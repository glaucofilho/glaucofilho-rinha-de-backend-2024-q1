from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IllegalStateChangeError, NoResultFound

from core import get_database_session
from queries import INSERIR_CREDITO_SQL, INSERIR_DEBITO_SQL
from schemas import (
    NoCliente,
    NoLimite,
    TransacaoInputSchema,
    TransacaoOutputSchema,
)

router = APIRouter()


@router.post(
    "/clientes/{cliente_id}/transacoes",
    responses={
        404: {"model": NoCliente},
        422: {"model": NoLimite},
        200: {"model": TransacaoOutputSchema},
    },
)
async def post_transacao(cliente_id: int, transacao: TransacaoInputSchema):
    """
    Rota para registrar uma nova transação para um cliente.

    Parâmetros:
    - cliente_id: O ID do cliente para o qual a transação será registrada.
    - transacao: O objeto TransacaoInputSchema contendo os detalhes da transação a ser registrada.

    Retorna:
    - TransacaoOutputSchema: O objeto TransacaoOutputSchema representando o resultado da transação.

    Lança:
    - HTTPException 404: Se o cliente não for encontrado.
    - HTTPException 422: Se a transação não puder ser concluída devido a um limite de crédito insuficiente.
    """

    try:
        async with get_database_session() as session:
            if transacao.tipo == "d":
                result = await session.execute(
                    INSERIR_DEBITO_SQL,
                    {
                        "cliente_id": cliente_id,
                        "valor": transacao.valor,
                        "descricao": transacao.descricao,
                    },
                )
            else:
                result = await session.execute(
                    INSERIR_CREDITO_SQL,
                    {
                        "cliente_id": cliente_id,
                        "valor": transacao.valor,
                        "descricao": transacao.descricao,
                    },
                )
            await session.commit()
            saldo, limite = result.fetchone()

    except NoResultFound:
        raise HTTPException(status_code=404, detail=NoCliente().message)
    except IllegalStateChangeError:
        raise HTTPException(status_code=422, detail=NoLimite().message)

    return TransacaoOutputSchema(limite=limite, saldo=saldo)
