from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import NoResultFound

from core import get_database_session
from queries import CONSULTA_EXTRATO_SQL, CONSULTA_LIMITES_SQL
from schemas import (
    ExtratoSchema,
    NoCliente,
    SaldoSchema,
    UltimasTransacoesSchema,
)

router = APIRouter()


@router.get(
    "/clientes/{cliente_id}/extrato",
    responses={404: {"model": NoCliente}, 200: {"model": ExtratoSchema}},
)
async def get_extrato(cliente_id: int):
    """
    Rota para obter o extrato de transações de um cliente.

    Parâmetros:
    - cliente_id: O ID do cliente cujo extrato de transações será obtido.

    Retorna:
    - ExtratoSchema: O objeto ExtratoSchema representando o extrato de transações do cliente.

    Lança:
    - HTTPException 404: Se o cliente não for encontrado.
    """

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
    except NoResultFound:
        raise HTTPException(status_code=404, detail=NoCliente().message)

    transacoes = [UltimasTransacoesSchema(**data) for data in transacoes_data]
    return ExtratoSchema(
        saldo=SaldoSchema(limite=limite, total=montante),
        ultimas_transacoes=transacoes,
    )
