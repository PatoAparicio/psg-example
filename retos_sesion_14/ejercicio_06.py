print("Crear una función que reciba una lista de números y devuelva una lista con los números pares y otra lista con los números impares")

def separar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros = input("Ingrese números separados por comas (ej: 1,2,3,4,5): ")

lista_numeros = [int(x.strip()) for x in numeros.split(",")]
pares, impares = separar(lista_numeros)
print(f"Números originales: {numeros}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
