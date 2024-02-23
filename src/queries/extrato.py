from sqlalchemy import text

CONSULTA_EXTRATO_SQL = text(
    "SELECT * FROM obter_ultimas_transacoes(:cliente_id);"
)
