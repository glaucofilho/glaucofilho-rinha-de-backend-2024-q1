from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from core import settings

# Cria a string de conexão com o banco de dados usando as configurações fornecidas
connection_string = (
    f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}"
    f"@{settings.db_address}:{str(settings.db_port)}/{settings.db_name}"
)

# Cria um mecanismo de banco de dados assíncrono usando a string de conexão
engine: AsyncEngine = create_async_engine(connection_string)

# Define uma classe de sessão baseada em coroutines usando AsyncSession
# e configura alguns comportamentos padrão
Session: AsyncSession = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine,
)
