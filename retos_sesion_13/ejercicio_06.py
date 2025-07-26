print("Crea un ciclo infinito que reciba un número por teclado y verifique si el número es múltiplo de 7. La ejecución termina si se ingresa el número 0")
while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    if num % 7 == 0:
        print(f"{num} es múltiplo de 7")
    else:
        print(f"{num} no es múltiplo de 7")