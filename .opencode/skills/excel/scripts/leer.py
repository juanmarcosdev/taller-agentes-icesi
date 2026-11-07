"""Muestra una hoja de Excel como texto separado por |."""
import sys

from comun import leer_filas

encabezado, filas = leer_filas(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
print(" | ".join(encabezado))
for fila in filas:
    print(" | ".join("" if fila[c] is None else str(fila[c]) for c in encabezado))
print(f"\nTotal de filas: {len(filas)}")
