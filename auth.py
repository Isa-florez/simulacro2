# auth.py
import csv
from utils import reintentos_recursivos

ADMIN_CSV = "admin_access.csv"

def cargar_admin():
    try:
        with open(ADMIN_CSV, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for row in lector:
                return row
    except FileNotFoundError:
        return None

def prompt_login():
    admin = cargar_admin()
    if not admin:
        print("No se encontró admin_access.csv.")
        return False

    username = input("ID de administrador: ").strip()
    password = input("Contraseña: ").strip()
    if username == admin.get("username") and password == admin.get("password"):
        print("Acceso concedido.")
        return True
    print("Credenciales incorrectas.")
    return False

def login_recursive(intentos=3):
    return reintentos_recursivos(prompt_login, intentos)
