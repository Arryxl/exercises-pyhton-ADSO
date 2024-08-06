import math
message = "¡Hola! estoy aprendiendo Python."
name = "Juan Reyes"
formacion =  "ADSO"
edad = 16
estatura = 1.81
peso = 63

# print method 1
print(message, "\nMi nombre es:", name, "\nSoy de la formación:", formacion, "\ntengo:", edad, "años", "\nmido:", estatura, "\npeso:", peso, "kg")

# print method 2
print(f'{message}\nMi nombre es: {name}\nSoy de la formación: {formacion}\nTengo: {edad}\nMido: {estatura}\nPeso: {peso}.')

a = 17
b = 6

suma = a + b
resta = a - b
multiplicacion = a * b
cociente = a // b
residuo = a % b

print("Suma:", suma, "Resta:", resta, "Multiplicación:", multiplicacion, "Division cociente:", cociente, "División residuo:", residuo)
print(f'Suma: {suma}, resta: {resta}, multiplicacion: {multiplicacion}, División cociente: {cociente}, División residuo: {residuo}')


# Ejercicio pidiendo datos por teclado

numero1 = int(input("Digíte un valor: "))
numero2 = int(input("Digíte otro valor: "))
print(f'Suma: {numero1+numero2}, resta: {numero1-numero2}, multiplicacion: {numero1*numero2}, División cociente: {numero1/numero2}, División residuo: {numero1%numero2}')



numero1 = int(input("Digíte un valor: "))
numero2 = int(input("Digíte otro valor: "))
operacion = input("Qué operación desea realizar?: ")
 
if operacion == "suma":
    print(f"El resultado de la suma es: {numero1+numero2}")
else:
    if operacion == "resta":
        print(f"El resultado de la resta es: {numero1-numero2}")
    else:
        if operacion == "multiplicacion":
            print(f"El resultado de la multiplicacion es: {numero1*numero2}")
        else:
            if operacion == "division":
                print(f"El resultado de la división es: {numero1/numero2}")
            else:
                print("Colocaste mal la operación deseada.")
                