#!/bin/bash

# Verifica si el archivo .env existe
if [ ! -f .env ]; then
    echo ".env file not found!"
    exit 1
fi

# Lee las variables de entorno desde el archivo .env
export $(grep -v '^#' .env | xargs)

# Ejecuta Flyway con las variables cargadas
flyway migrate
