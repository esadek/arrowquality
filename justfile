test:
    uv run pytest

lint:
    uv run ruff check

format:
    uv run ruff format

docs:
    uv run mkdocs serve
