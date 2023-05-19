install:
	poetry install

gendiff:
	poetry run gendiff

build: #check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

check: selfcheck test lint

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

rebase:
	git pull --rebase