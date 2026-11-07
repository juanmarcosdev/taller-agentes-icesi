"""Suma una columna de un CSV y lista las filas sin valor.

Uso: python calcular.py ARCHIVO.csv --sumar COLUMNA
Reemplace este calculo por el de su proceso. Pruebelo en la terminal antes de darselo a un agente.
"""
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("archivo")
parser.add_argument("--sumar", required=True)
args = parser.parse_args()

with open(args.archivo, encoding="utf-8-sig", newline="") as f:
    muestra = f.read(2048)
    f.seek(0)
    filas = list(csv.DictReader(f, dialect=csv.Sniffer().sniff(muestra, delimiters=",;")))

total, vacias = 0, []
for fila in filas:
    valor = (fila.get(args.sumar) or "").strip()
    if valor:
        total += float(valor)
    else:
        vacias.append(next(iter(fila.values())))

print(f"Filas: {len(filas)}")
print(f"Total de {args.sumar}: ${round(total):,}".replace(",", "."))
print(f"Filas sin {args.sumar}: {', '.join(vacias) if vacias else 'ninguna'}")
