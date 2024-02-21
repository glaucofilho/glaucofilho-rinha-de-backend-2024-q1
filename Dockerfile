FROM python:3.11-slim
WORKDIR /app
RUN pip install poetry
COPY src/ /app/
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN find /app -type d -name __pycache__ -exec rm -r {} +
CMD ["python", "main.py"]