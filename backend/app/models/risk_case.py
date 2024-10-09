from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class RiskCase:
    device_id: str
    contract_id: str
    category: str
    risk_score: float
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
