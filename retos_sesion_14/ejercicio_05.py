print("Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene.")
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador
cadena=input("Ingrese una cadena: ")
print(f"La cadena tiene {contar_vocales(cadena)} vocales")