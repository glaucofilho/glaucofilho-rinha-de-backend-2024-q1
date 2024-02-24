from sqlalchemy import CHAR, TIMESTAMP, VARCHAR, Column, Integer

from core import settings


class TransacoesModel(settings.DBBaseModel):
    """
    Modelo de dados para a tabela 'transacoes' no banco de dados.

    Esta classe define a estrutura da tabela 'transacoes', incluindo os tipos de dados
    e as restrições para cada coluna.

    Atributos:
    - id: Um inteiro que representa o identificador único da transação (chave primária).
          Este campo é obrigatório.
    - cliente_id: Um inteiro que representa o identificador único do cliente associado à transação.
                  Este campo é obrigatório.
    - valor: Um inteiro que representa o valor da transação em centavos.
             Este campo é obrigatório.
    - realizada_em: Um timestamp que representa o momento em que a transação foi realizada.
                    Este campo é obrigatório.
    - descricao: Uma string que representa a descrição da transação.
                 Este campo é obrigatório e tem no máximo 10 caracteres.
    - tipo: Uma string que representa o tipo de transação (crédito ou débito).
            Este campo é obrigatório e tem exatamente 1 caractere.

    """

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
