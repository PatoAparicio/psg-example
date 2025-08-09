print("Crea un programa que simule el funcionamiento de un cajero automático solicitando al usuario un monto a retirar. Si el monto ingresado es mayor al saldo disponible, el programa debe lanzar una excepción personalizada que indique que no hay fondos suficientes. Además, si el monto ingresado es mayor a 1000, debe lanzarse una excepción genérica que advierta que el monto excede el límite permitido por transacción.")
class FondosInsuficientesError(Exception):
    pass

class LimiteExcedidoError(Exception):
    pass

def cajero_automatico():
    saldo = 1000.00
    
    while True:
        try:
            print(f"\nSaldo disponible: ${saldo:.2f}")
            monto = input("Ingrese monto a retirar ('salir' para terminar): ")
            
            if monto == "salir":
                print("Gracias por usar nuestro cajero.")
                break
            
            monto = float(monto)
            
            if monto > 1000:
                raise LimiteExcedidoError("El monto excede el límite de $1000 por transacción")
            if monto > saldo:
                raise FondosInsuficientesError("Fondos insuficientes")
            if monto <= 0:
                raise ValueError("El monto debe ser positivo")
            
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
        except FondosInsuficientesError as e:
            print(f"Error: {e}")
        except LimiteExcedidoError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

cajero_automatico()