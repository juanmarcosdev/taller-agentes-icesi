"""Compara las cifras de un informe .docx con los dos archivos de Excel."""
import re
import sys
from pathlib import Path

from docx import Document

sys.path.insert(0, str(Path(__file__).parents[2] / "excel" / "scripts"))
from comun import leer_filas  # noqa: E402

informe, resumen, casos = sys.argv[1:4]
doc = Document(informe)
texto = " ".join(p.text for p in doc.paragraphs)
texto += " " + " ".join(c.text for t in doc.tables for r in t.rows for c in r.cells)
numeros = set(re.findall(r"\d+", re.sub(r"(?<=\d)[.,](?=\d{3}\b)", "", texto)))
errores = []

_, filas = leer_filas(resumen)
for fila in filas:
    sede = str(fila["Sede"])
    monto = str(fila["Monto total"])
    if sede not in ("TOTAL",) and sede not in texto:
        errores.append(f"Falta la sede {sede}")
    if monto not in numeros:
        errores.append(f"Falta el monto {monto} de {sede}")

_, escalados = leer_filas(casos)
for fila in escalados:
    if str(fila["ID"]) not in texto:
        errores.append(f"Falta el caso {fila['ID']}")

for e in errores:
    print(f"ERROR: {e}")
print("RESULTADO: ERROR" if errores else f"RESULTADO: OK ({len(filas)} filas y {len(escalados)} casos revisados)")
