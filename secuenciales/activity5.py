## Solicitamos los datos requeridos.
valor_producto = int(input("Ingrese el costo del producto: "))
descuento = int(input("Ingrese el descuento del producto: "))

## Hacemos la operacion y el total.
operacion = valor_producto * (descuento / 100)
total = valor_producto - operacion

## Imprimimos el resultado
print(f"La compra fue un total de {valor_producto}, con un descuento del {descuento}% y el valor final a pagar es: {total}.")