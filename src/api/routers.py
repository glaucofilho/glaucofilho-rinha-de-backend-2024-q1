from fastapi import APIRouter

from .endpoints_validados.clientes import router as clientes_router
from .endpoints_validados.extrato import router as extrato_router
from .endpoints_validados.transacoes import router as transacoes_router

api_router = APIRouter()

api_router.include_router(clientes_router, prefix="", tags=["Lista clientes"])
api_router.include_router(transacoes_router, prefix="", tags=["Transacoes"])
api_router.include_router(extrato_router, prefix="", tags=["Extrato"])
