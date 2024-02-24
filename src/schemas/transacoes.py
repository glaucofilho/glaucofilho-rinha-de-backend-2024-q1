from enum import Enum

from pydantic import BaseModel, Field


class TipoTransacao(str, Enum):
    """
    Enumeração para representar os tipos de transação.

    Possíveis valores são:
    - c: Crédito
    - d: Débito
    """

    c = "c"
    d = "d"


class TransacaoInputSchema(BaseModel):
    """
    Esquema de dados para representar uma transação de entrada realizada pelo cliente.

    Atributos:
    - valor: Um inteiro que representa o valor da transação em centavos.
             Este campo é obrigatório.
    - tipo: Um objeto do TipoTransacao que representa o tipo de transação (crédito ou débito).
            Este campo é obrigatório.
    - descricao: Uma string que representa a descrição da transação realizada.
                 Deve ter no máximo 10 caracteres e no mínimo 1 caractere.
                 Este campo é obrigatório.
    """

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
    """
    Esquema de dados para representar uma transação de saída.

    Atributos:
    - limite: Um inteiro que representa o limite de crédito em centavos do cliente.
              Este campo é obrigatório.
    - saldo: Um inteiro que representa o saldo após a transação em centavos do cliente.
             Este campo é obrigatório.
    """

    limite: int = Field(
        examples=[100000],
        description="Limite de credito em centavos do cliente.",
    )
    saldo: int = Field(
        examples=[-9098],
        description="Saldo apos transacao em centavos do cliente.",
    )
