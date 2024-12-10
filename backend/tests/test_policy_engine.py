from app.schemas.risk import ContractContext, PredictionSignal
from app.services.policy_engine import LegalRiskPolicyEngine, PolicyWeights


def test_policy_engine_generates_high_risk() -> None:
    engine = LegalRiskPolicyEngine(PolicyWeights(model_confidence=0.9, sla_sensitivity=0.00005))
    signal = PredictionSignal(device_id="dev-1", component="pump", failure_probability=0.8)
    contract = ContractContext(
        contract_id="c-1",
        repair_sla_hours=4,
        sla_penalty_per_hour=9000,
        regulatory_tier="critical",
    )

    result = engine.evaluate(signal, contract)

    assert result.category in {"high", "critical"}
    assert result.risk_score > 0.65
