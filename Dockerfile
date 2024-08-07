FROM python:3.12.3-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY deposit_app /app/deposit_app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "deposit_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]