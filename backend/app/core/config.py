from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Enterprise SOC Platform"
    app_version: str = "0.1.0"
    app_description: str = "Enterprise Security Operations Platform"

    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
