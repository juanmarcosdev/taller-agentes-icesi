"""Agrupa por una columna, suma los montos y guarda el resumen en un .xlsx."""
import argparse
from collections import defaultdict

from openpyxl import Workbook

from comun import a_numero, leer_filas

p = argparse.ArgumentParser()
p.add_argument("archivo")
p.add_argument("--agrupar", required=True)
p.add_argument("--sumar", required=True)
p.add_argument("--salida", required=True)
a = p.parse_args()

_, filas = leer_filas(a.archivo)
grupos = defaultdict(lambda: {"solicitudes": 0, "monto": 0, "sin_dato": 0})
for fila in filas:
    g = grupos[str(fila[a.agrupar])]
    g["solicitudes"] += 1
    monto = a_numero(fila[a.sumar])
    if monto is None:
        g["sin_dato"] += 1
    else:
        g["monto"] += monto

libro = Workbook()
hoja = libro.active
hoja.title = "Resumen"
hoja.append([a.agrupar, "Solicitudes", "Monto total", "Sin dato de monto"])
for nombre in sorted(grupos):
    g = grupos[nombre]
    hoja.append([nombre, g["solicitudes"], g["monto"], g["sin_dato"]])
total = [sum(g[k] for g in grupos.values()) for k in ("solicitudes", "monto", "sin_dato")]
hoja.append(["TOTAL", *total])
libro.save(a.salida)

for fila in hoja.iter_rows(values_only=True):
    print(" | ".join(str(c) for c in fila))
