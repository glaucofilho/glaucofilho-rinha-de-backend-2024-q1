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
    montante: int = Field(
        examples=[-25000],
        description="Montante em centavos do cliente.",
    )
