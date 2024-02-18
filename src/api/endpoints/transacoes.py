from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IllegalStateChangeError, NoResultFound

from core import get_database_session
from queries import INSERIR_TRANSACAO_SQL
from schemas import TransacaoInputSchema, TransacaoOutputSchema

router = APIRouter()


@router.post(
    "/clientes/{cliente_id}/transacoes", response_model=TransacaoOutputSchema
)
async def post_transacao(cliente_id: int, transacao: TransacaoInputSchema):
    try:
        async with get_database_session() as session:
            result = await session.execute(
                INSERIR_TRANSACAO_SQL,
                {
                    "cliente_id": cliente_id,
                    "valor": transacao.valor,
                    "descricao": transacao.descricao,
                    "tipo": transacao.tipo,
                },
            )
            await session.commit()
            limite, saldo = result.fetchone()
            return TransacaoOutputSchema(limite=limite, saldo=saldo)
    except NoResultFound:
        raise HTTPException(404)
    except IllegalStateChangeError:
        raise HTTPException(422)
