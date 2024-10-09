from pydantic import BaseModel, Field


class PredictionSignal(BaseModel):
    device_id: str
    component: str
    failure_probability: float = Field(ge=0.0, le=1.0)


class ContractContext(BaseModel):
    contract_id: str
    repair_sla_hours: int = Field(gt=0)
    sla_penalty_per_hour: float = Field(ge=0)
    regulatory_tier: str = Field(pattern="^(standard|critical|restricted)$")


class RiskRequest(BaseModel):
    signal: PredictionSignal
    contract: ContractContext


class LegalRiskAssessment(BaseModel):
    risk_score: float = Field(ge=0.0, le=1.0)
    category: str
    rationale: list[str]


class RiskResponse(BaseModel):
    assessment: LegalRiskAssessment
    recommended_action: str
