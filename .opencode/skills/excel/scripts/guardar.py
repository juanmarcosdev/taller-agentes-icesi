"""Crea un .xlsx a partir de un JSON {"Hoja": [[...], [...]]}."""
import json
import sys

from openpyxl import Workbook

with open(sys.argv[1], encoding="utf-8") as f:
    datos = json.load(f)

libro = Workbook()
libro.remove(libro.active)
for nombre, filas in datos.items():
    hoja = libro.create_sheet(nombre[:31])
    for fila in filas:
        hoja.append(fila)
libro.save(sys.argv[2])
print(f"Guardado {sys.argv[2]}")
