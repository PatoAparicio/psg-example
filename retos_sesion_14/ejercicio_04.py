print("Crear una función anónima para obtener el valor absoluto de un número.")
absoluto = lambda x: x if x >= 0 else -x
n=int(input ("Ingrese un número: "))
print(f"El valor absoluto es: {absoluto(n)}") 