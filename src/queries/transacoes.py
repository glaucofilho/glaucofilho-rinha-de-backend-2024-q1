from sqlalchemy import text

INSERIR_DEBITO_SQL = text(
    "SELECT * FROM inserir_debito(:cliente_id, :valor, :descricao)"
)

INSERIR_CREDITO_SQL = text(
    "SELECT * FROM inserir_credito(:cliente_id, :valor, :descricao)"
)
