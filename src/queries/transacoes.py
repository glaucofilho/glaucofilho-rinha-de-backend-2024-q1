from sqlalchemy import text

INSERIR_TRANSACAO_SQL = text(
    "WITH nova_transacao AS ("
    "    INSERT INTO transacoes (cliente_id, valor, descricao, tipo) "
    "    VALUES (:cliente_id, :valor, :descricao, :tipo) "
    "    RETURNING cliente_id"
    ") "
    "SELECT c.limite, c.fatura - :valor AS nova_fatura "
    "FROM clientes c WHERE c.id = :cliente_id"
)
