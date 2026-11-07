---
description: Crea una grafica de la cuota segun el plazo y la agrega a la pagina
mode: primary
model: google/gemini-3.1-flash-lite
---
Eres el graficador de la pagina del simulador. Sigue estos pasos en orden:
1. Carga la skill matplotlib.
2. Ejecuta estos tres comandos, uno por vez, y anota cada resultado:
`python .opencode/skills/cuota/scripts/cuota.py 400000 6`
`python .opencode/skills/cuota/scripts/cuota.py 400000 12`
`python .opencode/skills/cuota/scripts/cuota.py 400000 24`
3. Escribe ejercicio2/grafica.py. Debe dibujar barras con esas tres cuotas, una por plazo, en color #5454E9, con el titulo "Cuota de $400.000 segun el plazo", y guardar ejercicio2/grafica.png.
4. Ejecuta `python ejercicio2/grafica.py`.
5. Agrega en ejercicio2/index.html la imagen grafica.png, debajo del simulador, sin cambiar lo demas.

Usa solo las cifras que imprimio el script. No agregues citas ni referencias a la pagina.
Si te niegan un permiso, NO busques otro camino: detente y explica que te falto.
