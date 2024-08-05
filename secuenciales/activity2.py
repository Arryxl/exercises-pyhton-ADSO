## Solicitamos al usuario que ingrese la altura y base de su rectágulo.
altura = int(input("Introduce la altura de tu rectángulo: "))
base = int(input("Introduce la base de tu rectángulo: "))

## Hacemos la fórmula del perímetro y del área.
perimetro = 2 * (altura + base)
area = base * altura

## Imprimimos los resultados de ambas fórmulas.
print(f"El perímetro de tu rectángulo es: {perimetro}. \nEl área de tu rectángulo es: {area}.")