print("De la siguiente tupla de estudiantes, imprime las felicitaciones a los estudiantes que aprobaron el curso con una nota mayor o igual a 51")
estudiantes = [('Miguel', 51), ('Daniel', 80), ('Virginia', 90), ('Franco', 40), ('Flabio', 30)]
for nombre, nota in estudiantes:
    if nota >= 51:
        print(f"Felicidades {nombre}, aprobaste con {nota}!")