import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.exc import IllegalStateChangeError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from core import DatabaseSession


@asynccontextmanager
async def get_database_session() -> AsyncGenerator:
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
