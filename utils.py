# utils.py
from datetime import datetime

def print_header(text):
    print("\n" + "=" * 6 + f" {text} " + "=" * 6)

def pausar():
    input("\nPresiona ENTER para continuar...")

def concatenar_listas(*args):
    resultado = []
    for lst in args:
        resultado.extend(lst)
    return resultado

def reintentos_recursivos(prompt_fn, intentos):
    if intentos <= 0:
        return False
    ok = prompt_fn()
    if ok:
        return True
    return reintentos_recursivos(prompt_fn, intentos - 1)

def mostrar_clasificacion(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
