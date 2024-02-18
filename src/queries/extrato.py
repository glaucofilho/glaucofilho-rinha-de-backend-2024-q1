from sqlalchemy import text

CONSULTA_SALDO_SQL = text(
    "SELECT limite, fatura FROM clientes c WHERE c.id = :id LIMIT 1"
)


CONSULTA_TRANSACOES_SQL = text(
    "SELECT valor, tipo, descricao, realizada_em FROM transacoes t WHERE t.cliente_id = :cliente_id ORDER BY t.realizada_em DESC LIMIT 10"
)
