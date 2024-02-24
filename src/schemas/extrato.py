from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field

from .transacoes import TransacaoInputSchema


class TipoTransacao(str, Enum):
    """
    Enumeração para representar os tipos de transação.
    Possíveis valores são:
    - c: Crédito
    - d: Débito
    """

    c = "c"
    d = "d"


class UltimasTransacoesSchema(TransacaoInputSchema):
    """
    Esquema de dados para representar as últimas transações de um cliente.
    Herda de TransacaoInputSchema.
    Atributos:
    - realizada_em: Um datetime que representa o timestamp da transação.
                    Este campo é obrigatório.
    """

    realizada_em: datetime = Field(
        examples=[datetime.utcnow()],
        description="Timestamp da transacao.",
    )


class SaldoSchema(BaseModel):
    """
    Esquema de dados para representar o saldo de um cliente.
    Atributos:
    - total: Um inteiro que representa o saldo após uma transação em centavos do cliente.
            Este campo é obrigatório.
    - data_extrato: Um datetime que representa o timestamp do extrato.
                    Este campo é opcional e possui um valor padrão de datetime.utcnow().
    - limite: Um inteiro que representa o limite de crédito em centavos do cliente.
            Este campo é obrigatório.
    """

    total: int = Field(
        examples=[-9098],
        description="Saldo apos transacao em centavos do cliente.",
    )
    data_extrato: datetime = Field(
        examples=[datetime.utcnow()],
        description="Timestamp do extrato.",
        default_factory=datetime.utcnow,
    )
    limite: int = Field(
        examples=[100000],
        description="Limite de credito em centavos do cliente.",
    )


class ExtratoSchema(BaseModel):
    """
    Esquema de dados para representar o extrato de um cliente.
    Atributos:
    - saldo: Um objeto SaldoSchema que representa o saldo do cliente.
            Este campo é obrigatório.
    - ultimas_transacoes: Uma lista de objetos UltimasTransacoesSchema que representam as últimas transações do cliente.
                        Este campo é obrigatório.
    """

    saldo: SaldoSchema
    ultimas_transacoes: List[UltimasTransacoesSchema]
