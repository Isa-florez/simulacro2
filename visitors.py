# visitors.py
from storage import leer_csv, escribir_csv, agregar_fila
from utils import ahora
from typing import Dict, List

VISITANTES_CSV = "visitantes.csv"
CAMPOS = ["id", "nombre", "especie", "estado"]

def cargar_visitantes():
    return leer_csv(VISITANTES_CSV)

def ids_unicos(visitantes):
    return set(v["id"] for v in visitantes if v.get("id"))

def generar_id(visitantes):
    ids = ids_unicos(visitantes)
    n = 1
    while True:
        candidate = f"V{n:04d}"
        if candidate not in ids:
            return candidate
        n += 1

def registrar_visitante():
    visitantes = cargar_visitantes()
    nuevo_id = generar_id(visitantes)
    nombre = input("Nombre: ").strip()
    especie = input("Especie: ").strip()
    estado = "Activo"
    fila = {"id": nuevo_id, "nombre": nombre, "especie": especie, "estado": estado}
    agregar_fila(VISITANTES_CSV, fila, CAMPOS)
    print(f"Visitante registrado {nuevo_id} ({ahora()})")

def listar_visitantes():
    visitantes = cargar_visitantes()
    if not visitantes:
        print("No hay visitantes registrados.")
        return
    for v in visitantes:
        print((v.get("id",""), v.get("nombre",""), v.get("especie",""), v.get("estado","")))

def buscar_visitante():
    visitantes = cargar_visitantes()
    idb = input("ID a buscar: ").strip()
    for v in visitantes:
        if v.get("id") == idb:
            print("Encontrado:", v)
            return
    print("No encontrado.")

def actualizar_estado():
    visitantes = cargar_visitantes()
    idb = input("ID: ").strip()
    for v in visitantes:
        if v.get("id") == idb:
            v["estado"] = "Retirado" if v.get("estado","Activo")=="Activo" else "Activo"
            escribir_csv(VISITANTES_CSV, visitantes, CAMPOS)
            print("Estado actualizado.")
            return
    print("No existe.")

def eliminar_visitante():
    visitantes = cargar_visitantes()
    idb = input("ID: ").strip()
    for v in visitantes:
        if v.get("id") == idb:
            v["estado"] = "Eliminado"
            escribir_csv(VISITANTES_CSV, visitantes, CAMPOS)
            print("Marcado Eliminado.")
            return
    print("No encontrado.")

def estadisticas_visitantes():
    visitantes = cargar_visitantes()
    total = len(visitantes)
    por_especie = {}
    estados = {}
    especies_set = set()
    for v in visitantes:
        esp = v.get("especie","Desconocida")
        especies_set.add(esp)
        por_especie[esp] = por_especie.get(esp,0)+1
        estado = v.get("estado","Activo")
        estados[estado] = estados.get(estado,0)+1

    print("Total:", total)
    print("Por especie:", por_especie)
    print("Estados:", estados)
    print("Especies únicas:", tuple(especies_set))
