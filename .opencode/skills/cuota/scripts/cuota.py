"""Calcula la cuota mensual con tasa fija de 1,2 %."""
import sys

monto, meses = float(sys.argv[1]), int(sys.argv[2])
i = 0.012
cuota = monto * i / (1 - (1 + i) ** (-meses))
print(f"${round(cuota):,}".replace(",", "."))
