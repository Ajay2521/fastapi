from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_username: str
    db_pwd: str
    secret_key: str
    algorithm: str
    expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
