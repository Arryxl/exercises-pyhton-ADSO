## Ejercicio 5
"""
Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
de la compra el valor del descuento y el valor final a pagar.
"""

## Solicitamos los datos requeridos.
valor_producto = int(input("Ingrese el costo del producto: "))
descuento = int(input("Ingrese el descuento del producto: "))

## Hacemos la operacion y el total.
operacion = valor_producto * (descuento / 100)
total = valor_producto - operacion

## Imprimimos el resultado
print(f"La compra fue un total de {valor_producto}, con un descuento del {descuento}% y el valor final a pagar es: {total}.")