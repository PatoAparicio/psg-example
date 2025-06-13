print("Con las notas de un estudiante durante un semestre Genera una tupla con los resultados y calcula el promedio para saber si aprobó o no el semestre utiliza")
notas=(10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
longitud = len(notas)
suma = sum(notas)
promedio=suma/longitud
print("El promedio del alumno es: ", promedio)
print("El alumno está reprobado")