from fastapi import APIRouter
from fastapi.responses import Response
from sqlalchemy.exc import IllegalStateChangeError, NoResultFound

from core import get_database_session
from queries import INSERIR_CREDITO_SQL, INSERIR_DEBITO_SQL
from schemas import TransacaoInputSchema, TransacaoOutputSchema

router = APIRouter()


@router.post(
    "/clientes/{cliente_id}/transacoes"  # , response_model=TransacaoOutputSchema
)
async def post_transacao(cliente_id: int, transacao: TransacaoInputSchema):
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
            return TransacaoOutputSchema(limite=limite, saldo=saldo)
    except NoResultFound:
        return Response(status_code=404)
    except IllegalStateChangeError:
        return Response(status_code=422)
