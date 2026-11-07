# Simulador de prestamo de bienestar

Pagina de una sola vista para que un asociado estime su cuota mensual. Datos de ejemplo, no es una oferta real.

## Campos
- Monto del prestamo, en pesos.
- Plazo en meses: 6, 12 o 24.
- Boton "Calcular cuota".

## Calculo
Tasa mensual fija de 1,2 %. Con M = monto, i = 0,012 y n = meses:

cuota = M * i / (1 - (1 + i)^(-n))

Muestra la cuota sin decimales y con separador de miles, por ejemplo $35.990.

## Limite de autonomia
- Si el monto es igual o mayor a $500.000, NO muestres una cuota. Muestra: "Este monto requiere la revision de una persona del area de credito."
- Si el monto esta vacio o no es positivo, muestra: "Ingresa un monto valido."

## Diseno
Limpio y legible, tarjeta centrada, color principal #5454E9. Debe verse bien en celular.

## Lista de chequeo
1. Existe el campo de monto.
2. Existe el selector de plazo con 6, 12 y 24 meses.
3. Con 400.000 a 12 meses la cuota es $35.990.
4. Con 500.000 no muestra cuota y muestra el mensaje de revision.
5. Con el monto vacio muestra el mensaje de monto valido.
6. El CSS usa el color #5454E9.
