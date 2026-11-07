# Plantilla: su propio equipo de agentes

Copie esta carpeta `plantilla/` fuera del kit, renómbrela con el nombre de su proceso y ábrala en OpenCode con **Add project**. Así OpenCode carga sus agentes y no los del taller.

La plantilla ya funciona con un ejemplo: suma la columna `Monto` de `entradas/datos.csv` y escribe un resumen. Pruébela tal como está y luego reemplace cada pieza por la de su proceso. El Apéndice D de la guía explica cada paso.

## Qué hay en cada archivo

| Archivo | Qué cambia usted |
|---|---|
| `AGENTS.md` | Las reglas de su proceso: qué datos maneja, qué decide una persona y el tono |
| `opencode.json` | Los permisos. Todo empieza en `deny`; agregue solo lo que el equipo necesita |
| `entradas/` | Sus datos de entrada. Use datos ficticios o anonimizados |
| `salidas/` | Donde el equipo deja los entregables |
| `.opencode/skills/mi-calculo/SKILL.md` | Cuándo usar la skill (`description`) y cómo (cuerpo) |
| `.opencode/skills/mi-calculo/scripts/calcular.py` | La cuenta de su proceso. Pruébela en la terminal antes de dársela a un agente |
| `.opencode/agents/calculador.md` | Un trabajador: ejecuta un comando y reporta |
| `.opencode/agents/redactor.md` | Un trabajador: escribe el entregable con las cifras que recibe |
| `.opencode/agents/coordinador.md` | El coordinador: no trabaja, delega en orden y solo a quien tiene permiso |
| `.opencode/commands/procesar.md` | Crea el comando `/procesar` que lanza al coordinador |

## Pruébela

1. En una terminal dentro de la carpeta: `python .opencode/skills/mi-calculo/scripts/calcular.py entradas/datos.csv --sumar Monto`
2. En OpenCode: `/connect` con su clave de Gemini, luego `/reload`.
3. **New session**, escriba `/procesar`, pulse Enter, escriba `noviembre` y envíe.
4. Cuando pida permiso para escribir en `salidas/`, lea el cambio y pulse **Allow once**.

## Si sus datos están en Excel

Copie la carpeta `.opencode/skills/excel` del kit a su proyecto y agregue a `opencode.json` los permisos `shell` de sus scripts, igual que en el `opencode.json` del kit.
