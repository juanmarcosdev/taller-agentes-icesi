"""Crea un .docx a partir de un JSON con titulo y secciones."""
import json
import sys

from docx import Document

with open(sys.argv[1], encoding="utf-8") as f:
    datos = json.load(f)

doc = Document()
doc.add_heading(datos["titulo"], 0)
for seccion in datos["secciones"]:
    doc.add_heading(seccion["titulo"], 1)
    for parrafo in seccion.get("parrafos", []):
        doc.add_paragraph(parrafo)
    tabla = seccion.get("tabla")
    if tabla:
        t = doc.add_table(rows=len(tabla), cols=len(tabla[0]))
        t.style = "Light Grid Accent 1"
        for i, fila in enumerate(tabla):
            for j, valor in enumerate(fila):
                t.cell(i, j).text = str(valor)
doc.save(sys.argv[2])
print(f"Guardado {sys.argv[2]}")
