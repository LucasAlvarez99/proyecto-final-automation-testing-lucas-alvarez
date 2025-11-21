import csv
import json
from pathlib import Path
import os

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def leer_csv(nombre_archivo):
    # Ubicación real del proyecto (1 nivel arriba de utils/)
    base_dir = Path(__file__).resolve().parent.parent
    ruta = base_dir / "datos" / nombre_archivo

    if not ruta.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")

    with open(ruta, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)