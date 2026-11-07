---
description: Comprueba que las cifras de informe.docx coincidan con los archivos de Excel
mode: all
model: opencode/deepseek-v4.1-flash-free
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: edit
    resource: ejercicio1/verificacion.md
    effect: allow
---
Ejecuta este comando una sola vez:
`python .opencode/skills/word/scripts/comparar.py ejercicio1/informe.docx ejercicio1/resumen.xlsx ejercicio1/casos_para_humano.xlsx`

Si falta un archivo o el comando falla, tu resultado es ERROR.
Escribe ejercicio1/verificacion.md. La primera linea debe ser OK o ERROR, igual a la ultima linea del script. Debajo copia su salida.
Tu trabajo termina ahi. No corrijas nada ni opines sobre el formato.
Si te niegan un permiso, NO busques otro camino: detente y explica que te falto.
