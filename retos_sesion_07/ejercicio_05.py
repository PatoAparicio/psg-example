print("Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas")
palabra=str(input("Ingrese una cadena: "))
palabra_limpia = palabra.replace(" ", "").lower()
resultado=palabra_limpia==palabra_limpia[::-1]
print("La palabra es palindroma: ", resultado)