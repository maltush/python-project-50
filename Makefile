install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff -h:
	python3 gendiff/scripts/gendiff.py -h


