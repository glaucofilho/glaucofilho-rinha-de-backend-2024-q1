from fastapi import APIRouter
from fastapi.responses import Response
from sqlalchemy.exc import NoResultFound

from core import get_database_session
from queries import CONSULTA_EXTRATO_SQL, CONSULTA_LIMITES_SQL
from schemas import ExtratoSchema, SaldoSchema, UltimasTransacoesSchema

router = APIRouter()


@router.get(
    "/clientes/{cliente_id}/extrato"
)  # , response_model=ExtratoSchema)
async def get_extrato(cliente_id: int):
    try:
        async with get_database_session() as session:
            result = await session.execute(
                CONSULTA_EXTRATO_SQL,
                {
                    "cliente_id": cliente_id,
                },
            )
            transacoes = result.fetchall()
            transacoes_data = [row._asdict() for row in transacoes]

            if len(transacoes_data) == 0:
                result = await session.execute(
                    CONSULTA_LIMITES_SQL,
                    {
                        "id": cliente_id,
                    },
                )
                limite, montante = result.fetchone()
            else:
                limite, montante = (
                    transacoes_data[0]["limite"],
                    transacoes_data[0]["montante"],
                )
            transacoes = [
                UltimasTransacoesSchema(**data) for data in transacoes_data
            ]
            return ExtratoSchema(
                saldo=SaldoSchema(limite=limite, total=montante),
                ultimas_transacoes=transacoes,
            )
    except NoResultFound:
        return Response(status_code=404)
