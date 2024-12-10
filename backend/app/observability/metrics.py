from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("risk_api_requests_total", "Total number of risk api requests")
POLICY_EVALUATION_TIME = Histogram("risk_policy_evaluation_seconds", "Policy engine execution latency")
