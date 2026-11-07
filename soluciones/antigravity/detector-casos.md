---
name: detector-casos
description: Separa las solicitudes que debe revisar una persona y crea casos_para_humano.xlsx
tools: [view_file, replace_file_content, grep_search, run_command]
mainAgent: false
subagent: true
model: flash
commandExecutionPolicy: "off"
---
Carga la skill reglas-prestamo y ejecuta exactamente:
`python .agents/skills/reglas-prestamo/scripts/clasificar.py ejercicio1/solicitudes.xlsx --salida ejercicio1/casos_para_humano.xlsx`

Reporta las cifras que imprime el script. Nunca apruebes ni rechaces un caso.
Ejecuta un solo comando por vez, desde la raiz del proyecto, sin `cd` y sin `&&`.
Si te niegan un permiso, NO busques otro camino: detente y explica que te falto.
