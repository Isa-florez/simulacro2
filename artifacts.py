# artifacts.py
from storage import leer_csv, escribir_csv, agregar_fila

ARTEFACTOS_CSV = "artefactos.csv"
CAMPOS = ["codigo", "descripcion", "rareza", "estatus"]

def cargar_artefactos():
    return leer_csv(ARTEFACTOS_CSV)

def codigo_unico(arts):
    return set(a["codigo"] for a in arts if a.get("codigo"))

def generar_codigo(arts):
    ids = codigo_unico(arts)
    n = 1
    while True:
        c = f"A{n:05d}"
        if c not in ids:
            return c
        n+=1

def registrar_artefacto():
    arts = cargar_artefactos()
    codigo = generar_codigo(arts)
    desc = input("Descripción: ").strip()
    rareza = input("Rareza (Bajo/Medio/Alto/Prohibido): ").strip().title()
    est = input("Estatus (Almacenado/En Estudio/Destruido): ").strip().title()
    fila = {"codigo":codigo,"descripcion":desc,"rareza":rareza,"estatus":est}
    agregar_fila(ARTEFACTOS_CSV, fila, CAMPOS)
    print("Registrado", codigo)

def listar_artefactos():
    arts = cargar_artefactos()
    if not arts:
        print("No hay artefactos registrados.")
        return
    for a in arts:
        print((a.get("codigo",""), a.get("descripcion",""), a.get("rareza",""), a.get("estatus","")))

def buscar_artefacto():
    arts = cargar_artefactos()
    c = input("Código: ").strip()
    for a in arts:
        if a.get("codigo")==c:
            print("Encontrado:", a)
            return
    print("No existe.")

def clasificar_artefactos(**kwargs):
    arts = cargar_artefactos()
    filtrados = arts
    for k,v in kwargs.items():
        filtrados = [a for a in filtrados if a.get(k,"").lower()==v.lower()]
    if not filtrados:
        print("No hay artefactos con esos filtros.")
        return
    for a in filtrados:
        print(a)

def estadisticas_artefactos():
    arts = cargar_artefactos()
    rarezas={}
    ests={}
    for a in arts:
        r=a.get("rareza","Desconocida"); s=a.get("estatus","Desconocido")
        rarezas[r]=rarezas.get(r,0)+1
        ests[s]=ests.get(s,0)+1
    print("Rarezas:", rarezas)
    print("Estatus:", ests)

def eliminar_artefacto():
    arts = cargar_artefactos()
    c = input("Código: ").strip()
    for a in arts:
        if a.get("codigo")==c:
            a["estatus"]="Destruido"
            escribir_csv(ARTEFACTOS_CSV, arts, CAMPOS)
            print("Marcado destruido.")
            return
    print("No existe.")
