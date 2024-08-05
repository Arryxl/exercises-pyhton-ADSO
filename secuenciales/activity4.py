## Ejercicio 4
"""
Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.
"""

## Solicitamos los datos requeridos.
vendedor = str(input("Inserta el nombre del vendedor: "))
sueldo = input("Inserta su sueldo: ")
comision = input("Inserta la comisión de las ventas realizadas: ")

## Hacemos la suma para definir el sueldo total del vendedor.
total = sueldo + comision

## Imprimimos los resultados.
print(f"El vendedor {vendedor} tiene un sueldo de {sueldo}, durante el mes obtuvo una comisión de {comision} y el valor final a pagar es: {total}.")