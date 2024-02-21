from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import NoResultFound

from core import get_database_session
from queries import CONSULTA_SALDO_SQL, CONSULTA_TRANSACOES_SQL
from schemas import ExtratoSchema, SaldoSchema, UltimasTransacoesSchema

router = APIRouter()


@router.get(
    "/clientes/{cliente_id}/extrato"
)  # , response_model=ExtratoSchema)
async def get_extrato(cliente_id: int):
    try:
        async with get_database_session() as session:
            result = await session.execute(
                CONSULTA_TRANSACOES_SQL,
                {
                    "cliente_id": cliente_id,
                },
            )
            transacoes = result.fetchall()
            transacoes_data = [row._asdict() for row in transacoes]
            transacoes = [
                UltimasTransacoesSchema(**data) for data in transacoes_data
            ]
            result = await session.execute(
                CONSULTA_SALDO_SQL,
                {
                    "id": cliente_id,
                },
            )
            limite, montante = result.fetchone()
            return ExtratoSchema(
                saldo=SaldoSchema(limite=limite, total=montante),
                ultimas_transacoes=transacoes,
            )
    except NoResultFound:
        raise HTTPException(404)
