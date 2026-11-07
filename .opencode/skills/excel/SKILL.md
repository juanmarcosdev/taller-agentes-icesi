---
name: excel
description: Lee archivos .xlsx, resume una columna de montos por grupo y guarda tablas en un .xlsx nuevo. Usala siempre que debas consultar o producir un archivo de Excel.
---
# Trabajar con Excel

Nunca hagas sumas de memoria: usa estos scripts.

## Leer una hoja
`python .opencode/skills/excel/scripts/leer.py ARCHIVO.xlsx`

## Resumir montos por grupo
`python .opencode/skills/excel/scripts/resumir.py ARCHIVO.xlsx --agrupar Sede --sumar Monto --salida RESUMEN.xlsx`

Crea el archivo y muestra los totales. Los montos vacios o ilegibles se cuentan aparte como `sin dato`.

## Guardar una tabla propia
1. Escribe un archivo JSON con esta forma: `{"Hoja": [["Columna A", "Columna B"], ["dato", 10]]}`
2. Ejecuta `python .opencode/skills/excel/scripts/guardar.py DATOS.json SALIDA.xlsx`
