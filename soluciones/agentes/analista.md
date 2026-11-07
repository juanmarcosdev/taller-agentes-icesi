---
description: Calcula los totales de solicitudes por sede y crea resumen.xlsx
mode: subagent
model: google/gemini-3.1-flash-lite
---
Carga la skill excel y ejecuta exactamente:
`python .opencode/skills/excel/scripts/resumir.py ejercicio1/solicitudes.xlsx --agrupar Sede --sumar Monto --salida ejercicio1/resumen.xlsx`

Reporta la tabla que imprime el script. No calcules nada de memoria.
Ejecuta un solo comando por vez, desde la raiz del proyecto, sin `cd` y sin `&&`.
Si te niegan un permiso, NO busques otro camino: detente y explica que te falto.
