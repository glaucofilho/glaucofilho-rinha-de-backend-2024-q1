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

CREATE OR REPLACE FUNCTION verificar_limite_transacao()
RETURNS TRIGGER AS $$
BEGIN
    PERFORM 1 FROM public.clientes WHERE id = NEW.cliente_id FOR UPDATE;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'NOUSER';
    END IF;
    IF NEW.tipo = 'd' AND (SELECT montante + limite FROM public.clientes WHERE id = NEW.cliente_id) < - NEW.valor THEN
        RAISE EXCEPTION 'NOLIMIT';
    ELSE
        UPDATE public.clientes SET montante = montante + NEW.valor WHERE id = NEW.cliente_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verificar_limite_antes_inserir_transacao
BEFORE INSERT ON public.transacoes
FOR EACH ROW
EXECUTE FUNCTION verificar_limite_transacao();


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
