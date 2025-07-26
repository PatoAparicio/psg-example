print("Imprimir los 20 primeros números que sean múltiplos de 2 y 5")
count = 0
num = 10
while count < 20:
    if num % 2 == 0 and num % 5 == 0:
        print(num)
        count += 1
    num += 10