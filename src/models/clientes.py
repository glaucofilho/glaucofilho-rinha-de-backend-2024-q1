from sqlalchemy import VARCHAR, Column, Integer

from core import settings


class ClientesModel(settings.DBBaseModel):
    __tablename__ = "clientes"

    id = Column(
        Integer,
        primary_key=True,
    )
    nome = Column(VARCHAR(22), unique=True)
    limite = Column(Integer)
    fatura = Column(Integer)
