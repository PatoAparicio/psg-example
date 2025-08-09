print("Crea un programa que permita construir una canasta de frutas solicitando ingresar frutas por teclado, una por una, y almacenándolas en una lista. El programa debe finalizar cuando se ingrese 'salir' Solo se permiten las siguientes frutas: 🍅, 🍇, 🍈, 🍉, 🍊, 🍌, 🍍, 🍑Si se ingresa una fruta no permitida, el programa debe lanzar una excepción personalizada que indique que la fruta no es válida.")

class FrutaNoValidaError(Exception):
    pass

def canasta():
    frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑']
    canasta = []
    
    while True:
        try:
            fruta = input("Ingrese una fruta ('salir' para terminar): ")
            if fruta == "salir":
                print("Salió de la canasta")
                break
            
            if fruta not in frutas_permitidas:
                raise FrutaNoValidaError("Fruta no permitida")
            
            canasta.append(fruta)
            print(f"Canasta actual: {canasta}")
            
        except FrutaNoValidaError as e:
            print(f"Error: {e}. Frutas permitidas: {', '.join(frutas_permitidas)}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    print(f"\nCanasta final: {canasta}")

canasta()