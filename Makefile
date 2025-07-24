install:
	uv sync

build:
	uv build


gendiff:
	gendiff/scripts/gendiff.py -h

package-install:
	uv tool install --force dist/*.whl
