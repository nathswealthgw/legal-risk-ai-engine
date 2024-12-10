import json
from pathlib import Path

records = [
    {"device_id": "dev-1001", "component": "pump", "temperature_c": 88.1, "vibration_mm_s": 7.8},
    {"device_id": "dev-1828", "component": "valve", "temperature_c": 74.3, "vibration_mm_s": 5.1},
]

Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/demo_events.json").write_text(json.dumps(records, indent=2))
