from typing import ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    api_name: str = "Rinha Backend 2024 - glaucofilho"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 1
    api_disable_docs: bool = True

    db_user: str = "root"
    db_pass: str = "1234"
    db_address: str = "localhost"
    db_port: int = 5432
    db_name: str = "root"

    log_level: str = "ERROR"

    DBBaseModel: ClassVar = declarative_base()

    class Config:
        env_file = ".env"


settings = Settings()
