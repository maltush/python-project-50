install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff:
	uv run python -m gendiff.scripts.gendiff -- …


