from typing import List

from fastapi import APIRouter, HTTPException

from core import get_database_session
from models import ClientesModel
from queries import CONSULTA_CLIENTE_SQL, CONSULTA_CLIENTES_SQL
from schemas import ClienteSchema, NoCliente

router = APIRouter()


@router.get("/clientes", response_model=List[ClienteSchema])
async def clientes():
    """
    Rota para obter todos os clientes.

    Obtém todos os clientes do banco de dados e os retorna como uma lista de objetos ClienteSchema.

    Retorna:
    - List[ClienteSchema]: Uma lista de objetos ClienteSchema representando todos os clientes.
    """

    async with get_database_session() as session:
        result = await session.execute(CONSULTA_CLIENTES_SQL)
        clientes: List[ClientesModel] = result.fetchall()
        return clientes


@router.get(
    "/clientes/{cliente_id}",
    responses={404: {"model": NoCliente}, 200: {"model": ClienteSchema}},
)
async def cliente(
    cliente_id: int,
):
    """
    Rota para obter um cliente pelo ID.

    Parâmetros:
    - cliente_id: O ID do cliente a ser obtido.

    Retorna:
    - ClienteSchema: O objeto ClienteSchema representando o cliente obtido.

    Lança:
    - HTTPException 404: Se o cliente não for encontrado.
    """

    async with get_database_session() as session:
        result = await session.execute(
            CONSULTA_CLIENTE_SQL, {"id": cliente_id}
        )
        cliente: ClientesModel = result.fetchone()
    if cliente is None:
        raise HTTPException(status_code=404, detail=NoCliente().message)

    return ClienteSchema(
        id=cliente.id,
        nome=cliente.nome,
        limite=cliente.limite,
        montante=cliente.montante,
    )
