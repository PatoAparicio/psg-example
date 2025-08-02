print("Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas. Las calificaciones son: 50, 75, 80, 91, 70")
def promedio(calificaciones):
    
    return sum(calificaciones) / len(calificaciones)

notas = [50, 75, 80, 91, 70]
print(f"El promedio es: {promedio(notas)}")