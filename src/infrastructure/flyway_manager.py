# src/infrastructure/flyway_manager.py
import subprocess
import os


def run_flyway_migrations():
    """Ejecuta las migraciones de Flyway"""
    try:
        # Ejecuta el comando flyway migrate
        result = subprocess.run(["flyway", "migrate"],
                                check=True, capture_output=True, text=True)
        print("Flyway Migraciones ejecutadas con éxito:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar migraciones de Flyway: {e.stderr}")


def check_flyway_status():
    """Verifica el estado de las migraciones de Flyway"""
    try:
        # Ver el estado de las migraciones
        result = subprocess.run(
            ["flyway", "info"], check=True, capture_output=True, text=True)
        print("Estado de las migraciones de Flyway:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el estado de las migraciones: {e.stderr}")
