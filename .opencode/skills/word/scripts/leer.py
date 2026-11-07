"""Muestra el texto y las tablas de un .docx."""
import sys

from docx import Document

doc = Document(sys.argv[1])
for parrafo in doc.paragraphs:
    if parrafo.text.strip():
        print(parrafo.text)
for tabla in doc.tables:
    for fila in tabla.rows:
        print(" | ".join(c.text for c in fila.cells))
