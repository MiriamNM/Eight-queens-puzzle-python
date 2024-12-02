# 👑👑👑👑 EIGHT-QUEENS-PUZZLE-PYTHON 👑👑👑👑

# Eight Queens Puzzle API

[The eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques.arquitectura hexagonal. 

## Challenges
- Develop the 8 queens algorithm in python.
- Use FastApi to build the api.
- Use ORM as flyway and make migrations.
Store the solutions in postgres

## Next steps
- Finish the backend where Flyway already works well.
- Implement the frontend.

## Requirements

- Docker y Docker Compose
- python
- venv
- postman 
- visual studio code

## Comandos

- Build: `make build`
- Rebuild: `make rebuild`
- Raise services: `make up`
- Run tests: `make test`

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

### Descripción de la estructura

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



### comandos para: crear y activar entorno de python y instalar dependencias

   ```bash
   # crear entorno de python
   make create-venv

   # activar entorno de python
   source venv/bin/activate

   # desactivar entorno de python
   deactivate

   # instalar dependencias
   make install
   ```

9. Comandos de Makefile para: compilar, iniciar, parar, reiniciar, status, reconstruir, logs, y bash

   ```bash
   # compila la imagen
   make build

   # levanta el contenedor
   make start

   # detiene el contenedor
   make stop

   # reinicia el contenedor
   make restart

   # muestra el status del contenedor
   make status

   # detiene, compila y levanta el contenedor del worker
   make rebuild

   # muestra los logs del contenedor
   make logs

   ```
10. Plataformas para realizar request http
   - Insomnia
   - Postman
   - curl
