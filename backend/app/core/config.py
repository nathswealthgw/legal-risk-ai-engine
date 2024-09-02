from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Legal Risk AI Engine"
    env: str = "dev"
    tf_serving_url: str = "http://localhost:8501/v1/models/failure_model:predict"
    model_confidence_weight: float = 0.8
    sla_sensitivity: float = 0.00002

    model_config = SettingsConfigDict(env_file=".env", env_prefix="RISK_")


settings = Settings()
