---
name: word
description: Crea y lee documentos de Word (.docx). Usala siempre que debas entregar o revisar un informe en Word.
---
# Trabajar con Word

## Crear un documento
1. Escribe un archivo JSON con esta forma:
```json
{
  "titulo": "Titulo del informe",
  "secciones": [
    {"titulo": "Resumen", "parrafos": ["Texto."], "tabla": [["Sede", "Monto"], ["Norte", 100]]}
  ]
}
```
`tabla` es opcional.
2. Ejecuta `python .opencode/skills/word/scripts/crear.py DATOS.json SALIDA.docx`

Las cifras del informe deben salir de los archivos, nunca de memoria.

## Leer un documento
`python .opencode/skills/word/scripts/leer.py ARCHIVO.docx`

## Comparar un informe con sus fuentes
`python .opencode/skills/word/scripts/comparar.py INFORME.docx RESUMEN.xlsx CASOS.xlsx`

Muestra lo que falta y termina con `RESULTADO: OK` o `RESULTADO: ERROR`.
