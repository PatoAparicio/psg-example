print('Crea una calculadora interactiva que solicite dos números por teclado y realice las operaciones de suma, resta, multiplicación y división. El programa debe seguir solicitando dos números hasta que se ingrese "salir". Se debe incluir el manejo de excepciones para evitar errores al ingresar datos no numéricos, al intentar dividir entre cero, o ante cualquier otro error inesperado.')

def calculadora():
    while True:
        try:
            entrada = input("Ingrese dos números ('salir' para terminar): ")
            if entrada.lower() == "salir":
                print("Salió de la calculadora")
                break
            
            numeros = entrada.split()
            if len(numeros) != 2:
                raise ValueError("Debe ingresar exactamente dos números")
            
            a = float(numeros[0])
            b = float(numeros[1])
            
            print(f"\nSuma: {a + b}")
            print(f"Resta: {a - b}")
            print(f"Multiplicación: {a * b}")
            try:
                print(f"División: {a / b}")
            except ZeroDivisionError:
                print("División: No se puede dividir entre cero")
            
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

calculadora()