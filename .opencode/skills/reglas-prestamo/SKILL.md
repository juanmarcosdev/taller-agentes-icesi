---
name: reglas-prestamo
description: Reglas de autonomia del prestamo de bienestar. Usala para decidir que solicitudes puede resolver el agente y cuales debe escalar a una persona.
---
# Reglas del prestamo de bienestar

Aplica las reglas con el script. No decidas caso por caso.

`python .opencode/skills/reglas-prestamo/scripts/clasificar.py ARCHIVO.xlsx --salida CASOS.xlsx`

| Condicion | Decision |
|---|---|
| Monto menor a $500.000, sin mora y sin alerta | Resuelve el agente |
| Monto igual o mayor a $500.000 | Escala a una persona |
| Mora o alerta legal | Escala a una persona |
| Monto vacio o ilegible | Escala a una persona como incompleto |

El archivo de salida trae solo los casos escalados, con su motivo. El agente nunca aprueba ni rechaza un caso escalado.
