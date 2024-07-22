build:
	rm -rf dist/*
	python -m build

upload:
	twine upload --skip-existing --repository testpypi dist/*

install:
	pip install -e .

test: install
	pytest --disable-warnings tests/

check:
	git add .
	pre-commit run

pip:
	pip install -r requirements.txt

update:
	pcu requirements.txt -u
	pre-commit autoupdate
