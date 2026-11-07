"""Cambia los modelos del equipo. Uso:

python .devcontainer/elegir_modelos.py MODELO_COORDINADOR [MODELO_TRABAJADORES]
"""
import re
import sys
from pathlib import Path

COORDINADORES = {"coordinador-informe", "coordinador-web", "graficador"}

if len(sys.argv) < 2:
    sys.exit(__doc__)
coordinador = sys.argv[1]
trabajadores = sys.argv[2] if len(sys.argv) > 2 else None

for carpeta in ("soluciones/agentes", ".opencode/agents"):
    for archivo in Path(carpeta).glob("*.md"):
        modelo = coordinador if archivo.stem in COORDINADORES else trabajadores
        if modelo:
            texto = archivo.read_text(encoding="utf-8")
            archivo.write_text(re.sub(r"^model: .*$", f"model: {modelo}", texto, count=1, flags=re.M), encoding="utf-8")

print(f"Coordinador: {coordinador}")
print(f"Trabajadores: {trabajadores or 'sin cambios'}")
print("Escriba /reload en OpenCode.")
