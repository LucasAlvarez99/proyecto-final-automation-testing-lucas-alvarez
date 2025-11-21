import csv
import os

def read_csv(file_name):
    """Lee un archivo CSV y retorna una lista de diccionarios."""
    path = os.path.join("data", file_name)
    data = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
