import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.exc import IllegalStateChangeError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from core import DatabaseSession


@asynccontextmanager
async def get_database_session() -> AsyncGenerator:
    """
    Gerenciador de contexto assíncrono para obter uma sessão do banco de dados.

    Esta função cria uma sessão do banco de dados usando a configuração definida em DatabaseSession,
    e retorna essa sessão. Se ocorrer uma exceção durante o uso da sessão, a função trata
    exceções específicas, como NoResultFound e IllegalStateChangeError, e registra outras exceções
    usando o módulo logging. A sessão é fechada após o uso.

    Retorna:
    - AsyncGenerator: Um gerador assíncrono que produz a sessão do banco de dados.

    """
    session: AsyncSession = DatabaseSession()

    try:
        yield session
    except Exception as e:
        if "NOUSER" in str(e):
            raise NoResultFound
        if "NOLIMIT" in str(e) or "NOUSER" in str(e):
            raise IllegalStateChangeError
        else:
            logging.exception("e: ")
        await session.rollback()
    finally:
        await session.close()
