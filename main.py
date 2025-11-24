# main.py
from auth import login_recursive
import visitors
import artifacts
from utils import print_header, pausar

def menu_visitantes():
    while True:
        print_header("VISITANTES")
        print("1 Registrar")
        print("2 Listar")
        print("3 Buscar")
        print("4 Actualizar")
        print("5 Eliminar")
        print("6 Estadísticas")
        print("7 Volver")
        o=input("Opción: ")
        if o=="1": visitors.registrar_visitante()
        elif o=="2": visitors.listar_visitantes()
        elif o=="3": visitors.buscar_visitante()
        elif o=="4": visitors.actualizar_estado()
        elif o=="5": visitors.eliminar_visitante()
        elif o=="6": visitors.estadisticas_visitantes()
        elif o=="7": break
        pausar()

def menu_artefactos():
    while True:
        print_header("ARTEFACTOS")
        print("1 Registrar")
        print("2 Listar")
        print("3 Buscar")
        print("4 Clasificar (kwargs)")
        print("5 Estadísticas")
        print("6 Eliminar")
        print("7 Volver")
        o=input("Opción: ")
        if o=="1": artifacts.registrar_artefacto()
        elif o=="2": artifacts.listar_artefactos()
        elif o=="3": artifacts.buscar_artefacto()
        elif o=="4":
            entrada = input("Filtros k=v (ej: rareza=Alto,estatus=Almacenado): ").strip()
            kwargs={}
            if entrada:
                for item in entrada.split(","):
                    if "=" in item:
                        k,v=item.split("=",1)
                        kwargs[k.strip()]=v.strip()
            artifacts.clasificar_artefactos(**kwargs)
        elif o=="5": artifacts.estadisticas_artefactos()
        elif o=="6": artifacts.eliminar_artefacto()
        elif o=="7": break
        pausar()

def main():
    print("GALACTIC LIBRARY KEEPER - Consola")
    if not login_recursive(3):
        print("Login fallido.")
        return
    while True:
        print_header("MENÚ PRINCIPAL")
        print("1 Visitantes")
        print("2 Artefactos")
        print("3 Salir")
        o=input("Opción: ")
        if o=="1": menu_visitantes()
        elif o=="2": menu_artefactos()
        elif o=="3": 
            print("Saliendo... ¡Que la Ruta te acompañe!")
            break

if __name__=="__main__":
    main()
