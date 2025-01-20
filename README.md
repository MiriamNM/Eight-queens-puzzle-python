# 👑👑👑👑 EIGHT-QUEENS-PUZZLE-PYTHON 👑👑👑👑

# Eight Queens Puzzle API

[The eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques.arquitectura hexagonal. 

## Challenges
- Develop the 8 queens algorithm in python.
- Use FastApi to build the api.
- Use ORM as flyway and make migrations.
Store the solutions in postgres

## Next steps
- 
- Return answers to solutions with pagination

## Requirements

- Docker y Docker Compose
- python
- venv
- postman 
- visual studio code

## Estructura

```bash
hight-queens-puzzle-python
├── .cz.toml
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yml
├── flyway.conf
├── pytest.ini
├── requirements.txt
├── src
│   ├── app.py
│   ├── application
│   │   ├── business.py
│   │   └── queens
│   │       └── eight_queens.py
│   ├── domain
│   │   ├── entities
│   │   │   └── queens
│   │   │       └── eight_queens.py
│   │   └── repositories
│   │       └── eight_queens_repository.py
│   └── infrastructure
│       └── entity_manager.py
└── tests
    └── application


```

### Description of the structure

- Dockerfile: file with the configuration to create the image of the worker service
- Makefile: file to facilitate the compilation of the containers
- docker-compose.yml: file with the configuration to start the worker service
- src: folder to store the service code
- app.py: initial file to run the service
- application: folder to store the service logic
- eight_queens.py: File with the service logic contains the queen algorithm.
- business.py: file with the service logic contains the function
- domain: folder to store the data classes, entities, repositories, etc.
- entities: folder to store the data classes
- eight_queens.py: file with the queens data class
- repositories: folder to store the repository classes
- eight_queens_repository.py: file with the queens repository class
- infrastructure: folder to store the logic to connect to external services such as databases, mail, cache, etc.
- entity_manager.py: file with the logic to connect to the database
- tests: folder to store the unit tests
- application: folder to store the tests service logic unit tests
- test_business.py: file with service logic unit tests



### Commands to: create and activate python environment and install dependencies

   ```bash
    # Create virtual environment
      create-venv:
         python -m venv venv
         @echo "Activate the virtual environment with 'source venv/bin/activate'"

      # Install dependencies
      Install: 
         pip install -r requirements.txt

      # To ensure all dependencies are correctly installed, especially uvicorn and fastapi.
      test-requirements:
         pip install --upgrade pip
         pip install -r requirements.txt
         uvicorn src.app:app --host 0.0.0.0 --port 8080 --reload
   ```

9. Makefile commands for: build, start, stop, restart, status, rebuild, logs, and bash

   ```bash 
      # Start services with Docker Compose
      up:
         docker-compose up -d

      # Stop services
      down:
         docker-compose down

      # Rebuild and restart all services
      restart: stop start

      # Rebuild the services and remove volumes and images
      rebuild: 
         docker-compose down --volumes --rmi all
         docker-compose --env-file .env up --build
         docker compose up -d

      # Check the status of services
      status:
         docker compose ps

      # Follow logs from services
      logs:
         docker compose logs -f

      # Access the database
      queens: 
         docker exec -it eight_queens_db psql -U mirichi -d eight_queens_db

      # Run migrations
      migrate:
         @echo "Migrating schema: public"
         docker-compose run --rm flyway migrate -schemas=public -locations=filesystem:/flyway/sql/migrations

      # Undo the last migration
      undo:
         @echo "Undoing migration on schema: public"
         docker-compose run --rm flyway undo -schemas=public -locations=filesystem:/flyway/sql/migrations
   ```
10. Platforms to make http requests
   - Insomnia
   - Postman
   - curl

11. POST: http://localhost:8080/queens/
![post](https://raw.githubusercontent.com/MiriamNM/Eight-queens-puzzle-python/refs/heads/main/public/assets/Captura%20de%20pantalla%202024-12-03%20a%20la(s)%2011.41.58%E2%80%AFp.m..png)

12 GET: http://localhost:8080/queens/
![post](https://raw.githubusercontent.com/MiriamNM/Eight-queens-puzzle-python/refs/heads/main/public/assets/Captura%20de%20pantalla%202024-12-03%20a%20la(s)%2011.41.51%E2%80%AFp.m..png)

fastApi: http://localhost:8080/docs#/

12. Instructions for Configuring `pre-commit`

This project uses [pre-commit](https://pre-commit.com/) to automate the execution of Git hooks before making a commit. This ensures that quality tasks, such as code formatting, are performed before any changes are confirmed.
### Steps Description

1. **Install dependencies**: `pre-commit` is installed automatically along with other libraries when you run:
   ```bash
   pip install -r requirements.txt
2. Prepare changes: Add the modified files to the staging area using
   ```bash
      git add . 
      git add 'archivo'
3. Make the commit: Use the command to create a standardized commit message with Commitizen
   ```bash
      cz c 
      cz commit
4. Push the code: Send your changes to the remote repository using
   ```bash
      git push origin "branch"
- By following these steps, you ensure that commit messages follow a standard format and that the code passes quality checks before being pushed.

