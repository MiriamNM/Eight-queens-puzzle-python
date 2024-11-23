create-venv:
	python -m venv venv
	@echo "ejecutar el entorno virtual con 'source venv/bin/activate'"

Install: 
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Construir la imagen
build:
	docker build -t eight-queens-puzzle .

# Levantar los servicios con Docker Compose
up:
	docker-compose up -d

# Detener los servicios
down:
	docker-compose down

# Recostruir y reinicar todos los servicios
restart: stop start
rebuild: 
	docker compose down
	docker compose build
	docker compose up -d

# Ver el estado de los servicios
status:
	docker compose ps

logs:
	docker compose logs -f