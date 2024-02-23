from sqlalchemy import text

CONSULTA_CLIENTE_SQL = text(
    "SELECT id, nome, limite, montante FROM clientes c WHERE c.id = :id LIMIT 1"
)

CONSULTA_CLIENTES_SQL = text("SELECT id, nome, limite, montante FROM clientes")


CONSULTA_LIMITES_SQL = text(
    "SELECT limite, montante FROM clientes c WHERE c.id = :id LIMIT 1"
)
