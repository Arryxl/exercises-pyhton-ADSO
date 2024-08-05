estudiante = str(input("Inserte nombre del estudiante: "))
PromedioClase = int(input("Inserte el promedio de notas en clase: "))
PromedioFinal = int(input("Inserte la calificación del proyecto final: "))
PromedioParcial = int(input("Inserte el promedio de evaluaciones parciales: "))

opClase = PromedioClase * 0.3
opFinal = PromedioFinal * 0.5
opParcial = PromedioParcial * 0.2

notaFinal = opClase + opFinal + opParcial

print(f"La nota final de algoritmia del estudiante {estudiante} es: {notaFinal}")
