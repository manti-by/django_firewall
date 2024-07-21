build:
	python -m build

install:
	pip install dist/django_firewall-0.0.1.tar.gz

test: build install
	pytest --disable-warnings tests/

check:
	git add .
	pre-commit run

pip:
	pip install -r requirements.txt

update:
	pcu requirements.txt -u
	pre-commit autoupdate
