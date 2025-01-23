create-venv:
	python3.11 -m venv venv
	@echo "Entorno virtual creado con Python 3.11."
	@echo "Ejecuta 'source venv/bin/activate' para activarlo."

install: 
	pip install -r requirements.txt

#Para asegurar que todas las dependencias estan correctamente, sobretodo uvicorn y fastapi.
test-requirements:
	pip install --no-cache-dir -r requirements.txt
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

rebuild: 
	docker-compose down --volumes --rmi all
	docker-compose --env-file .env up --build
	docker compose up -d

# Ver el estado de los servicios
status:
	docker compose ps

logs:
	docker compose logs -f

# Ver la base de datos
queens: 
	docker exec -it eight_queens_db psql -U mirichi -d eight_queens_db

migrate:
	@echo "Migrando esquema: public"
	docker-compose run --rm flyway migrate -schemas=public -locations=filesystem:/flyway/sql/migrations

undo:
	@echo "Deshaciendo migración en esquema: public"
	docker-compose run --rm flyway undo -schemas=public -locations=filesystem:/flyway/sql/migrations
