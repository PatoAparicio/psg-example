print("Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado de la operación")
def calcular(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b if b != 0 else "Error: división por cero"
    else:
        return "Operación no válida"

num_1=int(input ("Ingrese el primer número: "))
num_2=int(input ("Ingrese el segundo número: "))
operacion=input ("Ingrese el signo de la operación: " )
print(f"El resultado es: {calcular(num_1, num_2, operacion)}")