set dotenv-load := true

check:
    @just lint
    @just format-check
    @just typecheck
    @just test

lint:
    uv run ruff check .

format:
    uv run ruff format .

format-check:
    uv run ruff format --check .

typecheck:
    uv run pyright .

test:
    uv run pytest

fix:
    uv run ruff check --fix .
