install:
	uv sync

build:
	uv build

gendiff:
	uv sync

package-install:
	uv tool install --force ../dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml
	

.PHONY: gendiff


