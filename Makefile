create-venv:
	python3.11 -m venv queens
	@echo "Entorno virtual creado con Python 3.11."
	@echo "Ejecuta 'source queens/bin/activate' para activarlo."

install: 
	export PYTHONPATH=$PYTHONPATH:/Users/mirichi/Documents/dev/Eight-queens-puzzle-python/src
	pip install -r requirements.txt

#Para asegurar que todas las dependencias estan correctamente, sobretodo uvicorn y fastapi.
test-requirements:
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

# Detener los servicios y levantar los servicios con Docker Compose
rebuild: 
	docker-compose down --volumes --rmi all
	docker-compose --env-file .env up --build