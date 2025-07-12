print("Ingresa una pregunta por teclado y almacena el valor en una tupla")
ingreso=input("Ingrese una pregunta ")
pregunta=(ingreso, )
concatenar = ('¿', ) + pregunta + ('?', )
print (concatenar)
repetir = concatenar*2
print (repetir)