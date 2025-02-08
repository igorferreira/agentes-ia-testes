.PHONY: setup install test run dev clean format activate deactivate build-windows build-linux start-mock

# Variáveis do ambiente virtual
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Criar ambiente virtual Python e atualizar pip
setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

# Instalar todas as dependências do requirements.txt
install: setup
	$(PIP) install -r requirements.txt

# Executar todos os testes unitários
test:
	$(PYTHON) -m pytest tests/

# Iniciar a aplicação
run:
	$(PYTHON) src/main.py

# Iniciar a aplicação em modo de desenvolvimento
# export BROWSER=/usr/bin/google-chrome && 
dev:
	export BROWSER=/usr/bin/google-chrome &&  streamlit run src/main.py --server.runOnSave true

run-mock:
	python mock/app.py

# Limpar arquivos temporários e caches
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete

# Formatar código usando black e isort
format:
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

# Ativar ambiente virtual
activate:
	. $(VENV)/bin/activate

# Desativar ambiente virtual
deactivate:
	deactivate

# Gerar executável para Windows com pyinstaller
build-windows:
	$(PIP) install pyinstaller
	pyinstaller --onefile --name registro_cauda_windows src/main.py

# Gerar executável para Linux com pyinstaller
build-linux:
	$(PIP) install pyinstaller
	pyinstaller --onefile --name registro_cauda_linux src/main.py

# Gerar executável para Windows com nativefier
build-win:
	npm install nativefier -g
	nativefier --name registro_cauda "http://localhost:8501/" --platform "windows" --verbose

# Gerar executável para Linux com nativefier
build-linx:
	npm install nativefier -g
	nativefier --name registro_cauda "http://localhost:8501/" --platform "linux" --verbose

# Lint the code
.PHONY: lint
lint: venv
	$(ACTIVATE) && flake8 .

# Run tests
.PHONY: test
test: venv
	$(ACTIVATE) && pytest

ativar:
	# Activate virtual environment
	. venv/bin/activate

libs:
	# Install dependencies
	pip install -r requirements.txt && playwright install

