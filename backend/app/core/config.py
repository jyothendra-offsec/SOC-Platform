from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Enterprise SOC Platform"
    app_version: str = "0.1.0"
    app_description: str = "Enterprise Security Operations Platform"

    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "soc_platform"
    database_user: str = "soc_admin"
    database_password: str = ""

    api_prefix: str = "/api/v1"
    log_level: str = "INFO"
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}"
            f"/{self.database_name}"
        )


settings = Settings()
