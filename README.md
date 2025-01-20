# 👑👑👑👑 EIGHT-QUEENS-PUZZLE-PYTHON 👑👑👑👑

# Eight Queens Puzzle API

[The eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques.arquitectura hexagonal. 

## Challenges
- Develop the 8 queens algorithm in python.
- Use FastApi to build the api.
- Use ORM as flyway and make migrations.
Store the solutions in postgres

## Next steps
- Return answers to solutions with pagination
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
   # create python environment
   make create-venv

   # activate python environment
   source venv/bin/activate

   # disable python environment
   deactivate

   # install dependencies
   make install
   ```

9. Makefile commands for: build, start, stop, restart, status, rebuild, logs, and bash

   ```bash
   # compile the image
   make build

   # llift the container
   make start

   # stops the container
   make stop

   # restart the container
   make restart

   # shows the status of the container
   make status

   # stops, builds and starts the worker container
   make rebuild

   # mshow container logs
   make logs

   # Show database
   make queens

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

12. Instrucciones para configurar `pre-commit`

Este proyecto usa [pre-commit](https://pre-commit.com/) para automatizar la ejecución de ganchos (hooks) de Git antes de realizar un commit. Esto garantiza que se realicen tareas de calidad de código, como el formateo del código, antes de que se confirme un cambio.


### Descripción de los pasos

1. **Instalar dependencias**: `pre-commit` se instala automáticamente junto con las demás librerías al ejecutar:
   ```bash
   pip install -r requirements.txt
2. Preparar los cambios: Añade los archivos modificados al área de preparación con: git add . o git add 'archivo'
3. Hacer el commit: Usa el comando para crear un mensaje de commit estandarizado con Commitizen: cz c o cz commit
4. Subir el código: Envía tus cambios al repositorio remoto con: git push origin "branch"

*** Con estos pasos, aseguras que los mensajes de commit sigan un formato estándar y que el código pase las verificaciones de calidad antes de ser enviado.

