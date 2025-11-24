# storage.py
import csv
from typing import List, Dict

def leer_csv(ruta: str) -> List[Dict[str, str]]:
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            return list(lector)
    except FileNotFoundError:
        return []

def escribir_csv(ruta: str, filas: List[Dict[str, str]], campos: List[str]):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)

def agregar_fila(ruta: str, fila: Dict[str, str], campos: List[str]):
    # Apendea una fila; si el archivo no existe, lo crea con encabezado
    need_header = not os.path.exists(ruta) if 'os' in globals() else True
    try:
        with open(ruta, "a", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            # escribir header si archivo vacío
            f.seek(0)
            if f.tell() == 0:
                escritor.writeheader()
            escritor.writerow(fila)
    except FileNotFoundError:
        escribir_csv(ruta, [fila], campos)
