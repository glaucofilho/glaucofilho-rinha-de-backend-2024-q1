from typing import List

from fastapi import APIRouter, HTTPException

from core import get_database_session
from models import ClientesModel
from queries import CONSULTA_CLIENTE_SQL, CONSULTA_CLIENTES_SQL
from schemas import ClienteSchema

router = APIRouter()


@router.get("/clientes", response_model=List[ClienteSchema])
async def clientes():
    async with get_database_session() as session:
        result = await session.execute(CONSULTA_CLIENTES_SQL)
        clientes: List[ClientesModel] = result.fetchall()
        return clientes


@router.get("/clientes/{cliente_id}", response_model=ClienteSchema)
async def cliente(
    cliente_id: int,
):
    async with get_database_session() as session:
        result = await session.execute(
            CONSULTA_CLIENTE_SQL, {"id": cliente_id}
        )
        cliente: ClientesModel = result.fetchone()
        if not cliente:
            raise HTTPException(status_code=404)
        return cliente
