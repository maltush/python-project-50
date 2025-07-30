install:
	uv sync

build:
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install --force ../dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest
	
.PHONY: gendiff


