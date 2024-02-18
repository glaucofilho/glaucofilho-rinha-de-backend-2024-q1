import logging

from fastapi import FastAPI

from api import api_router
from core import settings

docs_url = None if settings.api_disable_docs else "/docs"
redoc_url = None if settings.api_disable_docs else "/redoc"

app = FastAPI(title=settings.api_name, docs_url=docs_url, redoc_url=redoc_url)
app.include_router(api_router, prefix="")

logging.getLogger("fastapi").setLevel(settings.log_level)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host=settings.api_host,
        port=settings.api_port,
        log_level=settings.log_level.lower(),
        workers=settings.api_workers,
    )
