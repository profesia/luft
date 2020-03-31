.ONESHELL:
.PHONY: run init

VENV_NAME=venv
PYTHON=${VENV_NAME}/bin/python3
PIP=${VENV_NAME}/bin/pip3

init:
	python3 -m venv ${VENV_NAME}

clean:
	rm -rf ${VENV_NAME}/ .pytest_cache/ .git/

install:
	${PIP} install -e ".[bq,dev]"

initlocaltest:
	sudo mkdir -p /var/tmp && sudo ln -s ${GOOGLE_APPLICATION_CREDENTIALS} /var/tmp/key.json
    export LUFT_CONFIG=../airflow-dags/luft/test_luft.cfg

test:
	${VENV_NAME}/bin/pytest tests/test_bq*

dockerbuildprod:
	docker build -t luft:prod --target prod .

dockerbuilddev:
	docker build -t luft:dev --target dev .