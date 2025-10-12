from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str
    secret_key: str
    access_token_expire_minutes: int = 30

    # Nueva forma de definir configuración
    model_config = SettingsConfigDict(env_file="../../.env")

    # Construye automáticamente la URL de conexión
    @property
    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()
