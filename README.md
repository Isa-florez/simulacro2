# Galáctic Library Keeper - Simulacro

## Autor
Isabella

## Descripción
Proyecto simulado 'simulacro2' que implementa un gestor simple de visitantes y artefactos.
Persistencia en CSV para que la información sobreviva reinicios.

## Estructura
- main.py
- auth.py
- storage.py
- utils.py
- visitors.py
- artifacts.py
- admin_access.csv
- visitantes.csv
- artefactos.csv

## Cómo ejecutar
1. Coloca todos los archivos en la misma carpeta.
2. Ejecuta `python main.py`
3. Inicia sesión con:
   - username: admin
   - password: orbit123

## Uso de colecciones
- **Listas**: al leer CSV con `storage.leer_csv` se obtiene una lista de diccionarios.
- **Diccionarios**: cada visitante/artefacto es representado por un dict (fila).
- **Tuplas**: al mostrar listados, se imprimen tuplas para evitar modificaciones accidentales.
- **Sets**: se usan para manejar IDs únicos (funciones `ids_unicos`, `codigo_unico`).

## Funciones especiales
- `concatenar_listas(*args)` en `utils.py` usa *args.
- `clasificar_artefactos(**kwargs)` en `artifacts.py` usa **kwargs para filtrar por campos.
- `reintentos_recursivos` en `utils.py` es recursiva y se usa para reintentos de login en `auth.py`.

## Decisión sobre eliminación
- Por defecto se **marca** un visitante como "Eliminado" o un artefacto como "Destruido"
  en vez de borrar la fila físicamente. Esto preserva el historial y evita pérdida irreversible.

## Persistencia
- Lectura y escritura CSV mediante `storage.py`.
- Se garantiza que cada registro nuevo se guarda usando `agregar_fila` o `escribir_csv`.

## Mejoras futuras
- Validaciones más estrictas de entradas.
- Manejo de concurrencia y backups automáticos.
- Interfaz gráfica.
