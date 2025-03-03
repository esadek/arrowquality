test:
    uv run pytest

coverage:
    uv run pytest --cov=src

lint:
    uv run ruff check
    uv run mypy src/arrowquality tests --strict

format:
    uv run ruff format

docs:
    uv run mkdocs serve

clean:
    rm -rf */__pycache__ */*/__pycache__ .mypy_cache .pytest_cache .ruff_cache .coverage
