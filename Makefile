create-venv:
	python3.11 -m venv queens
	@echo "Entorno virtual creado con Python 3.11."
	@echo "Ejecuta 'source queens/bin/activate' para activarlo."

pip:
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	wget https://bootstrap.pypa.io/get-pip.py


install: 
	pip install -r requirements.txt
	@echo "Ejecuta: export PYTHONPATH=$PYTHONPATH:$(pwd)/src  antes de make test-requirements"

#Para asegurar que todas las dependencias estan correctamente, sobretodo uvicorn y fastapi.
test-requirements:
	export PYTHONPATH=$PYTHONPATH:/Users/mirichi/Documents/dev/Eight-queens-puzzle-python/src
	pip install --no-cache-dir -r requirements.txt
	uvicorn src.app:app --host 0.0.0.0 --port 8080 --reload


# Construir la imagen
build:
	docker build -t eight-queens-puzzle .
	@@ -23,9 +24,6 @@ up:

# Levantar los servicios con Docker Compose
up:
	docker-compose up -d

# Detener los servicios
down:
	docker-compose down

# Elimina volumenes e imagenes y vuelve a construir todo el contenedor
rebuild: 
	docker-compose down --volumes --rmi all
	docker-compose --env-file .env up --build

run-tests:
	pytest tests/test_app.py tests/test_eight_queens.py tests/test_eight_repository.py tests/test_entity_manager.py
