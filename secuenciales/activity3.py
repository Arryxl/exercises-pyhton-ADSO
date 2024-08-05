## Ejercicio 3

"""
Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los
números ingresado es: xxxx
"""

## Solicitamos al usuario que ingrese 3 números
valor1 = int(input("Inserta un número: "))
valor2 = int(input("Inserta otro número: "))
valor3 = int(input("Inserta un último número: "))

## Hacemos la operación para generar un promedio con los números obtenidos.
promedio = (valor1 + valor2 + valor3) / 34

## Imprimimos los resultados.
print(f"El promedio de {valor1} + {valor2} + {valor3} es igual a: {promedio}.")