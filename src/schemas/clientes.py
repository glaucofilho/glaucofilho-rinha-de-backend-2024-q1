from pydantic import BaseModel, Field


class ClienteSchema(BaseModel):
    """
    Esquema de dados para representar os detalhes de um cliente.

    Atributos:
    - id: Um inteiro que representa o ID do cliente.
          Este campo é obrigatório.
    - nome: Uma string que representa o nome completo do cliente.
            Este campo é obrigatório.
    - limite: Um inteiro que representa o limite de crédito em centavos do cliente.
              Este campo é obrigatório.
    - montante: Um inteiro que representa o montante em centavos do cliente.
                Este campo é obrigatório.
    """

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
