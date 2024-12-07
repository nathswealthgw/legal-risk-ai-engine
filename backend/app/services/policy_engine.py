from dataclasses import dataclass

from app.schemas.risk import ContractContext, LegalRiskAssessment, PredictionSignal


@dataclass
class PolicyWeights:
    model_confidence: float = 0.8
    sla_sensitivity: float = 0.00002


class LegalRiskPolicyEngine:
    def __init__(self, weights: PolicyWeights) -> None:
        self.weights = weights

    def evaluate(self, signal: PredictionSignal, contract: ContractContext) -> LegalRiskAssessment:
        base = signal.failure_probability * self.weights.model_confidence
        sla_factor = contract.sla_penalty_per_hour / max(contract.repair_sla_hours, 1)
        compliance_factor = 1.15 if contract.regulatory_tier in {"critical", "restricted"} else 1.0
        exposure = min(1.0, base + (sla_factor * self.weights.sla_sensitivity)) * compliance_factor

        category = (
            "critical"
            if exposure >= 0.85
            else "high"
            if exposure >= 0.65
            else "medium"
            if exposure >= 0.40
            else "low"
        )

        return LegalRiskAssessment(
            risk_score=round(min(exposure, 1.0), 4),
            category=category,
            rationale=[
                f"model_failure_probability={signal.failure_probability:.3f}",
                f"sla_penalty_per_hour={contract.sla_penalty_per_hour}",
                f"regulatory_tier={contract.regulatory_tier}",
            ],
        )

    @staticmethod
    def recommend_action(category: str) -> str:
        return {
            "critical": "Dispatch immediate intervention and trigger legal escalation.",
            "high": "Create risk case and schedule expedited repair.",
            "medium": "Monitor closely and prepare contingency notice.",
            "low": "Continue standard monitoring cycle.",
        }[category]
