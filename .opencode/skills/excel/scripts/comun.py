"""Funciones compartidas por los scripts de la skill excel."""
import re

from openpyxl import load_workbook


def leer_filas(ruta, hoja=None):
    libro = load_workbook(ruta, data_only=True)
    tabla = libro[hoja] if hoja else libro.worksheets[0]
    filas = list(tabla.iter_rows(values_only=True))
    encabezado = [str(c).strip() for c in filas[0]]
    return encabezado, [dict(zip(encabezado, f)) for f in filas[1:] if any(c is not None for c in f)]


def a_numero(valor):
    """Devuelve el monto como entero; acepta 450000 y '$450.000'. None si no se puede leer."""
    if isinstance(valor, bool) or valor is None:
        return None
    if isinstance(valor, (int, float)):
        return int(valor)
    limpio = re.sub(r"[^\d]", "", str(valor))
    return int(limpio) if limpio else None
