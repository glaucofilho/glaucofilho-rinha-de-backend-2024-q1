SET search_path = public;
SET client_encoding = 'UTF8';
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

CREATE TABLE public.clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(22) UNIQUE,
    limite INTEGER,
    montante INTEGER
);

CREATE TABLE public.transacoes (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES public.clientes(id),
    valor INTEGER,
    realizada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao VARCHAR(10),
    tipo CHAR(1)
);

CREATE OR REPLACE FUNCTION inserir_credito(cliente_id INT, valor INT, descricao VARCHAR)
RETURNS TABLE(novo_montante INT, cliente_limite INT) AS $$
DECLARE
    var_novo_montante INT;
    var_cliente_limite INT;
BEGIN

    -- Verifica se o cliente existe
    IF NOT EXISTS (SELECT 1 FROM public.clientes WHERE id = cliente_id) THEN
        RAISE EXCEPTION 'NOUSER';
    END IF;

    -- Obtém um bloqueio exclusivo para o cliente
    PERFORM pg_advisory_xact_lock(cliente_id);

    -- Insere a transação de crédito
    INSERT INTO public.transacoes (cliente_id, valor, descricao, tipo)
    VALUES (cliente_id, valor, descricao, 'c');

    -- Atualiza o saldo do cliente e retorna montante e limite
    UPDATE public.clientes
    SET montante = montante + valor
    WHERE id = cliente_id
    RETURNING montante, limite INTO var_novo_montante, var_cliente_limite;

    -- Retorna os valores
    RETURN QUERY SELECT var_novo_montante, var_cliente_limite;
END;
$$ LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION inserir_debito(cliente_id INT, valor INT, descricao VARCHAR)
RETURNS TABLE(novo_montante INT, cliente_limite INT) AS $$
DECLARE
    var_novo_montante INT;
    var_cliente_limite INT;
BEGIN
    -- Verifica se o cliente existe
    IF NOT EXISTS (SELECT 1 FROM public.clientes WHERE id = cliente_id) THEN
        RAISE EXCEPTION 'NOUSER';
    END IF;

    -- Obtém um bloqueio exclusivo para o cliente
    PERFORM pg_advisory_xact_lock(cliente_id);

    -- Verifica se o cliente tem saldo suficiente
    IF NOT EXISTS (
        SELECT 1 FROM public.clientes
        WHERE id = cliente_id AND montante - valor >= -limite
    ) THEN
        RAISE EXCEPTION 'NOLIMIT';
    END IF;

    -- Insere a transação de débito
    INSERT INTO public.transacoes (cliente_id, valor, descricao, tipo)
    VALUES (cliente_id, valor, descricao, 'd'); -- Note o valor negativo

    -- Atualiza o saldo do cliente e retorna montante e limite
    UPDATE public.clientes
    SET montante = montante - valor
    WHERE id = cliente_id
    RETURNING montante, limite INTO var_novo_montante, var_cliente_limite;

    -- Retorna os valores
    RETURN QUERY SELECT var_novo_montante, var_cliente_limite;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION obter_ultimas_transacoes(var_cliente_id INT)
RETURNS TABLE(valor INT, tipo CHAR, descricao VARCHAR, realizada_em TIMESTAMP, montante INT, limite INT) AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM public.clientes WHERE id = var_cliente_id) THEN
        RAISE EXCEPTION 'NOUSER';
    END IF;

    PERFORM pg_advisory_xact_lock(var_cliente_id);

    RETURN QUERY 
    SELECT t.valor, t.tipo, t.descricao, t.realizada_em, c.montante, c.limite
    FROM public.transacoes t
    JOIN public.clientes c ON t.cliente_id = c.id
    WHERE t.cliente_id = var_cliente_id
    ORDER BY t.id DESC
    LIMIT 10;
END;
$$ LANGUAGE plpgsql;




CREATE INDEX idx_transacoes_cliente_id ON public.transacoes(cliente_id);

CREATE INDEX idx_transacoes_realizada_em ON public.transacoes(realizada_em);

DO $$
BEGIN
  INSERT INTO public.clientes (nome, limite, montante)
  VALUES
    ('o barato sai caro', 1000 * 100, 0),
    ('zan corp ltda', 800 * 100, 0),
    ('les cruders', 10000 * 100, 0),
    ('padaria joia de cocaia', 100000 * 100, 0),
    ('kid mais', 5000 * 100, 0);
END; $$
