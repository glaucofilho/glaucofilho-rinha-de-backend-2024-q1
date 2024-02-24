from sqlalchemy import VARCHAR, Column, Integer

from core import settings


class ClientesModel(settings.DBBaseModel):
    """
    Modelo de dados para a tabela 'clientes' no banco de dados.

    Esta classe define a estrutura da tabela 'clientes', incluindo os tipos de dados
    e as restrições para cada coluna.

    Atributos:
    - id: Um inteiro que representa o identificador único do cliente (chave primária).
          Este campo é obrigatório.
    - nome: Uma string que representa o nome do cliente.
            Este campo é obrigatório e tem no máximo 22 caracteres. Deve ser único.
    - limite: Um inteiro que representa o limite de crédito em centavos do cliente.
              Este campo é obrigatório.
    - montante: Um inteiro que representa o montante em centavos do cliente.
                Este campo é obrigatório.

    """

    __tablename__ = "clientes"

    id = Column(
        Integer,
        primary_key=True,
    )
    nome = Column(VARCHAR(22), unique=True)
    limite = Column(Integer)
    montante = Column(Integer)
