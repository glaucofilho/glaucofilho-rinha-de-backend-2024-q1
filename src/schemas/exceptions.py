from pydantic import BaseModel


class NoCliente(BaseModel):
    """
    Modelo de dados para representar um erro de cliente não encontrado.
    """

    message: str = "Cliente not found"


class NoLimite(BaseModel):
    """
    Modelo de dados para representar um erro de limite insuficiente.
    """

    message: str = "No limite"
