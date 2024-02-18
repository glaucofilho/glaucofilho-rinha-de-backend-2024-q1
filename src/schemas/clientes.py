from pydantic import BaseModel, Field


class ClienteSchema(BaseModel):
    id: int = Field(examples=[2], description="Id inteiro do cliente.")
    nome: str = Field(
        examples=["zan corp ltda"], description="Nome completo do cliente."
    )
    limite: int = Field(
        examples=[80000],
        description="Limite de credito em centavos do cliente.",
    )
    fatura: int = Field(
        examples=[-25000],
        description="Fatura de credito em centavos do cliente.",
    )
