## Ejercicio 2

"""
Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
del rectángulo es: yyyy
"""

## Solicitamos al usuario que ingrese la altura y base de su rectágulo.
altura = int(input("Introduce la altura de tu rectángulo: "))
base = int(input("Introduce la base de tu rectángulo: "))

## Hacemos la fórmula del perímetro y del área.
perimetro = 2 * (altura + base)
area = base * altura

## Imprimimos los resultados de ambas fórmulas.
print(f"El perímetro de tu rectángulo es: {perimetro}. \nEl área de tu rectángulo es: {area}.")