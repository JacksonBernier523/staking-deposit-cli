VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3.8

help:
	@echo "clean - remove build and Python file artifacts"
	# Run with venv
	@echo "venv_deposit - run deposit cli with venv"
	@echo "venv_build - install basic dependencies with venv"
	@echo "venv_build_test - install testing dependencies with venv"
	@echo "venv_lint - check style with flake8 and mypy with venv"
	@echo "venv_test - run tests with venv"

clean:
	rm -rf venv/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name __pycache__ -exec rm -rf {} \;
	find . -name .mypy_cache -exec rm -rf {} \;
	find . -name .pytest_cache -exec rm -rf {} \;

$(VENV_NAME)/bin/activate: requirements.txt
	@test -d $(VENV_NAME) || python3 -m venv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python setup.py install
	${VENV_NAME}/bin/python -m pip install -r requirements.txt
	${VENV_NAME}/bin/python -m pip install -r requirements_test.txt
	@touch $(VENV_NAME)/bin/activate

venv_build: $(VENV_NAME)/bin/activate

venv_build_test: venv_build
	${VENV_NAME}/bin/python -m pip install -r requirements_test.txt

venv_test: venv_build_test
	$(VENV_ACTIVATE) && python -m pytest .

venv_lint: venv_build_test
	$(VENV_ACTIVATE) && flake8 --config=flake8.ini ./eth2deposit ./cli ./tests && mypy --config-file mypy.ini -p eth2deposit -p tests

venv_deposit: venv_build
	$(VENV_ACTIVATE) && python ./eth2deposit/deposit.py
