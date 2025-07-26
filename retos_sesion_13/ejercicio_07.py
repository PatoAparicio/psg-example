print("Crear una serie de números del 1 al 100, si el número es divisible entre 5 imprimir Fizz, si el número es divisible entre 7 imprimir Buzz, si el número es divisible entre 5 y 7 imprimir FizzBuzz")
for num in range(1, 101):
    if num % 5 == 0 and num % 7 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Fizz")
    elif num % 7 == 0:
        print("Buzz")
    else:
        print(num)