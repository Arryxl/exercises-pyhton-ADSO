## Solicitamos los datos requeridos.
vendedor = str(input("Inserta el nombre del vendedor: "))
sueldo = input("Inserta su sueldo: ")
comision = input("Inserta la comisión de las ventas realizadas: ")

## Hacemos la suma para definir el sueldo total del vendedor.
total = sueldo + comision

## Imprimimos los resultados.
print(f"El vendedor {vendedor} tiene un sueldo de {sueldo}, durante el mes obtuvo una comisión de {comision} y el valor final a pagar es: {total}.")