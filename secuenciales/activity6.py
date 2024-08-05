## Ejercicio adicional
"""
Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las
siguientes apreciaciones:
• Actividades en clase equivalen a un porcentaje de 30%
• Proyecto final 50%
• Evaluaciones parciales 20%
"""

## Pedimos al usuario el promedio de cada nota y el nombre del estudiante.
estudiante = str(input("Inserte nombre del estudiante: "))
PromedioClase = int(input("Inserte el promedio de notas en clase: "))
PromedioFinal = int(input("Inserte la calificación del proyecto final: "))
PromedioParcial = int(input("Inserte el promedio de evaluaciones parciales: "))


## Generamos el descuento para cada nota correspondida
opClase = PromedioClase * 0.3
opFinal = PromedioFinal * 0.5
opParcial = PromedioParcial * 0.2


## Sumamos el total
notaFinal = opClase + opFinal + opParcial


# Imprimimos la nota final
print(f"La nota final de algoritmia del estudiante {estudiante} es: {notaFinal}")
