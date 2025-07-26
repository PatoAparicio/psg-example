print("Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. La ejecución termina si la frase ingresada contiene la palabra salir")
while True:
    frase = input("Ingresa una frase (o 'salir' para terminar): ").lower()
    if "salir" in frase:
        break
    # Eliminar espacios y caracteres no alfanuméricos para mejor verificación
    limpia = ''.join(c for c in frase if c.isalnum())
    if limpia == limpia[::-1]:
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo.")