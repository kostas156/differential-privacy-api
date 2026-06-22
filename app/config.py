from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Anonify"
    app_version: str = "0.1.0"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    default_epsilon: float = 1.0
    default_sensitivity: float = 1.0

    model_config = {"env_file": ".env"}

settings = Settings()