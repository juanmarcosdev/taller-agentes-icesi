"""Aplica la matriz de escalamiento y guarda los casos para revision humana."""
import argparse
import sys
from pathlib import Path

from openpyxl import Workbook

sys.path.insert(0, str(Path(__file__).parents[2] / "excel" / "scripts"))
from comun import a_numero, leer_filas  # noqa: E402

UMBRAL = 500_000


def motivo(fila):
    monto = a_numero(fila["Monto"])
    if monto is None:
        return "Monto vacio o ilegible"
    if monto >= UMBRAL:
        return "Monto igual o mayor al umbral"
    if str(fila["Mora"]).strip().lower() in ("si", "sí"):
        return "Asociado en mora"
    alerta = str(fila["Alerta"] or "").strip().lower()
    if alerta not in ("", "ninguna"):
        return f"Alerta legal: {fila['Alerta']}"
    return None


p = argparse.ArgumentParser()
p.add_argument("archivo")
p.add_argument("--salida", required=True)
a = p.parse_args()

encabezado, filas = leer_filas(a.archivo)
escalados = [(f, motivo(f)) for f in filas if motivo(f)]

libro = Workbook()
hoja = libro.active
hoja.title = "Casos para humano"
hoja.append([*encabezado, "Motivo"])
for fila, razon in escalados:
    hoja.append([*(fila[c] for c in encabezado), razon])
libro.save(a.salida)

total, n = len(filas), len(escalados)
print(f"Total: {total}")
print(f"Resueltas por el agente: {total - n}")
print(f"Escaladas a una persona: {n}")
print(f"Tasa de resolucion: {round(100 * (total - n) / total)}%")
