from enum import Enum

from pydantic import BaseModel, Field


class TipoTransacao(str, Enum):
    c = "c"
    d = "d"


class TransacaoInputSchema(BaseModel):
    valor: int = Field(
        examples=[1000],
        description="Valor de transacao em centavos realizada pelo cliente.",
    )
    tipo: TipoTransacao = Field(
        examples=[TipoTransacao.c],
        description="Tipo de transacao realizada, credito ou debito.",
    )
    descricao: str = Field(
        max_length=10,
        min_length=1,
        examples=["descricao"],
        description="Descricao da transacao realizada.",
    )


class TransacaoOutputSchema(BaseModel):
    limite: int = Field(
        examples=[100000],
        description="Limite de credito em centavos do cliente.",
    )
    saldo: int = Field(
        examples=[-9098],
        description="Saldo apos transacao em centavos do cliente.",
    )
