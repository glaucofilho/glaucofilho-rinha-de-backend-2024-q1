from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field

from .transacoes import TransacaoInputSchema, TransacaoOutputSchema


class TipoTransacao(str, Enum):
    c = "c"
    d = "d"


class UltimasTransacoesSchema(TransacaoInputSchema):
    realizada_em: datetime = Field(
        examples=[datetime.utcnow()],
        description=["Timestamp da transacao."],
    )


class SaldoSchema(BaseModel):
    total: int = Field(
        examples=[-9098],
        description="Saldo apos transacao em centavos do cliente.",
    )
    data_extrato: datetime = Field(
        examples=[datetime.utcnow()],
        description=["Timestamp do extrato."],
        default_factory=datetime.utcnow,
    )
    limite: int = Field(
        examples=[100000],
        description="Limite de credito em centavos do cliente.",
    )


class ExtratoSchema(BaseModel):
    saldo: SaldoSchema
    ultimas_transacoes: List[UltimasTransacoesSchema]
