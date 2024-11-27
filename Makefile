create-venv:
	python -m venv venv
	@echo "ejecutar el entorno virtual con 'source venv/bin/activate'"

Install: 
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

#Para asegurar que todas las dependencias estan correctamente, sobretodo uvicorn y fastapi.
test-requirements:
	pip install --upgrade pip
	pip install -r requirements.txt
	uvicorn src.app:app --host 0.0.0.0 --port 8080 --reload

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
	docker-compose down --volumes --rmi all
	docker-compose --env-file .env up --build
	docker compose up -d

# Ver el estado de los servicios
status:
	docker compose ps

logs:
	docker compose logs -f

migrate:
	@echo "Migrando esquema: $(SCHEMA)"
	docker-compose run --rm flyway migrate -schemas=$(SCHEMA) -locations=filesystem:/flyway/sql/$(SCHEMA)/migrations

undo:
	@echo "Migrando esquema: $(SCHEMA)"
	docker-compose run --rm flyway undo -schemas=$(SCHEMA) -locations=filesystem:/flyway/sql/$(SCHEMA)/migrations