from sqlalchemy import CHAR, TIMESTAMP, VARCHAR, Column, Integer

from core import settings


class TransacoesModel(settings.DBBaseModel):
    __tablename__ = "transacoes"

    id = Column(
        Integer,
        primary_key=True,
    )
    cliente_id = Column(Integer)
    valor = Column(Integer)
    realizada_em = Column(TIMESTAMP)
    descricao = Column(VARCHAR(10))
    tipo = Column(CHAR(1))
