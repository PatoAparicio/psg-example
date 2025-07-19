print("Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicación y división. Las operaciones se ingresan por teclado separadas por comas")
entrada = input("Ingrese una operación (ej: 10, 5, +): ")
partes = [x.strip() for x in entrada.split(',')]

if len(partes) == 3:
        num1 = float(partes[0])
        num2 = float(partes[1])
        op = partes[2]
        
        if op == '+':
            print("Resultado: ", num1 + num2)
        elif op == '-':
            print("Resultado: ",num1 - num2)
        elif op == '*':
            print("Resultado: ",num1 * num2)
        elif op == '/':
            print("Resultado: ",num1 / num2 if num2 != 0 else "Error: División por cero")
        else:
            print("Operación no válida")
else:
    print("Formato incorrecto. Use: numero1, numero2, operación")