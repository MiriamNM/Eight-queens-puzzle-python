# 👑👑👑👑 EIGHT-QUEENS-PUZZLE-PYTHON 👑👑👑👑

# Eight Queens Puzzle API
[The eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques. 

## Challenges
- Develop the 8 queens algorithm in python, the project uses Python version 3.11.
- Use FastApi to build the api.
- Use ORM as flyway and make migrations.
- Store the solutions in postgres

## Next steps
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
	@@ -38,7 +34,6 @@ hight-queens-puzzle-python
├── src
│   ├── app.py
│   ├── application
│   │   └── queens
│   │       └── eight_queens.py
│   ├── domain
	@@ -48,15 +43,21 @@ hight-queens-puzzle-python
│   │   └── repositories
│   │       └── eight_queens_repository.py
│   └── infrastructure
│   │    └── entity_manager.py
│   └── utils
│        └── error_messages.py
│        └── serealize_queen.py
│        └── success_messages.py
└── tests
    └── test_app.py
    └── test_eight_queens.py
    └── test_eight_repository.py
    └── test_entity_manager.py


```

### Description of the structure
- Dockerfile: file with the configuration to create the image of the worker service
- Makefile: file to facilitate the compilation of the containers
- docker-compose.yml: file with the configuration to start the worker service
	@@ -75,69 +76,54 @@ hight-queens-puzzle-python
- tests: folder to store the unit tests
- application: folder to store the tests service logic unit tests
- test_business.py: file with service logic unit tests
- utils: Folder that stores auxiliary functions



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
      # To ensure all dependencies are correctly installed, especially uvicorn and fastapi.
      test-requirements

      # Start services with Docker Compose
      up

      # Stop services
      down

      # Rebuild the services and remove volumes and images
      rebuild

      # Check the status of services
      status

      # Follow logs from services
      logs

      # Access the database
      queens

      # Run migrations
      migrate

      # Undo the last migration
      undo
   ```
10. Platforms to make http requests
   - Insomnia