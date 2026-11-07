---
description: Revisa la pagina contra la lista de chequeo de los requisitos
mode: subagent
model: opencode/deepseek-v4.1-flash-free
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: edit
    resource: ejercicio2/revision.md
    effect: allow
---
Carga la skill cuota y ejecuta:
`python .opencode/skills/cuota/scripts/cuota.py 400000 12`

Nunca hagas esa cuenta de memoria: el resultado correcto es el que imprime el script.
Lee ejercicio2/requisitos.md, ejercicio2/index.html y ejercicio2/estilos.css.
Compara la formula del JavaScript con la formula de los requisitos, escrita letra por letra.
Revisa cada punto de la lista de chequeo.
Escribe en ejercicio2/revision.md una primera linea con OK o ERROR y, debajo, el resultado de cada punto.
Marca ERROR solo si la formula o un elemento de la pagina no coinciden con los requisitos.
No corrijas nada: solo informa.
Si te niegan un permiso, NO busques otro camino: detente y explica que te falto.
