default:
    just --list

test:
    uv run pytest -v

test-all:
    uv run nox -s tests

coverage:
    uv run pytest --cov=src

lint:
    uv run ruff check --fix

types:
    uv run mypy src/arrowquality tests --strict

types-all:
    uv run nox -s types

format:
    uv run ruff format

docs:
    uv run mkdocs serve

clean:
    rm -rf __pycache__ */__pycache__ */*/__pycache__
    rm -rf .pytest_cache .ruff_cache .mypy_cache .nox .coverage
