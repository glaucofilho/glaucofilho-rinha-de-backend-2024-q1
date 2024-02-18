from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from core import settings

connection_string = (
    f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}"
    f"@{settings.db_address}:{str(settings.db_port)}/{settings.db_name}"
)
engine: AsyncEngine = create_async_engine(connection_string)

Session: AsyncSession = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine,
)
