set dotenv-load := true

src_path := "src"

check:
    @just lint-check
    @just format-check
    @just type-check
    @just test

lint-check:
    uv run ruff check {{src_path}}

lint-fix:
    uv run ruff check --fix {{src_path}}

format-check:
    uv run ruff format --check {{src_path}}

format:
    uv run ruff format {{src_path}}

type-check:
    uv run pyright {{src_path}}

test:
    uv run pytest {{src_path}}
