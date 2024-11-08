from fastapi import APIRouter

from app.core.config import settings
from app.observability.metrics import POLICY_EVALUATION_TIME, REQUEST_COUNT
from app.schemas.risk import RiskRequest, RiskResponse
from app.services.policy_engine import LegalRiskPolicyEngine, PolicyWeights

router = APIRouter(prefix="/api/v1/risk", tags=["risk"])
policy_engine = LegalRiskPolicyEngine(
    PolicyWeights(
        model_confidence=settings.model_confidence_weight,
        sla_sensitivity=settings.sla_sensitivity,
    )
)


@router.post("/assess", response_model=RiskResponse)
async def assess_legal_risk(payload: RiskRequest) -> RiskResponse:
    REQUEST_COUNT.inc()
    with POLICY_EVALUATION_TIME.time():
        assessment = policy_engine.evaluate(payload.signal, payload.contract)
        action = policy_engine.recommend_action(assessment.category)
    return RiskResponse(assessment=assessment, recommended_action=action)
