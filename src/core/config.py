from typing import ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações para o aplicativo Rinha Backend 2024 - glaucofilho.

    Este objeto contém todas as configurações necessárias para executar o aplicativo,
    incluindo configurações da API e do banco de dados.

    Atributos:
    - api_name: O nome da API.
    - api_host: O endereço IP em que a API será hospedada.
    - api_port: A porta em que a API será executada.
    - api_workers: O número de trabalhadores da API.
    - api_disable_docs: Um sinalizador para desativar a geração automática de documentação da API.
    - db_user: O nome de usuário do banco de dados.
    - db_pass: A senha do banco de dados.
    - db_address: O endereço IP do banco de dados.
    - db_port: A porta do banco de dados.
    - db_name: O nome do banco de dados.
    - acess_logs: Um sinalizador para habilitar ou desabilitar o acesso aos logs.
    - log_level: O nível de registro dos logs.
    - debug_mode: Um sinalizador para habilitar ou desabilitar o modo de depuração.
    - reload: Um sinalizador para habilitar ou desabilitar a reinicialização automática do aplicativo.
    - DBBaseModel: Uma classe base declarativa para modelos de banco de dados.
    """

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

    acess_logs: bool = False
    log_level: str = "ERROR"
    debug_mode: bool = False
    reload: bool = False

    DBBaseModel: ClassVar = declarative_base()

    class Config:
        env_file = ".env"


settings = Settings()
