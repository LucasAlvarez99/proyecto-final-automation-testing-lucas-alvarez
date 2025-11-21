import csv
import os

def load_csv_data(file_name):
    """
    Lee un archivo CSV desde la carpeta /datos/ y devuelve una lista de diccionarios.
    """
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "datos", file_name)

    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data
