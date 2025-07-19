print("Tienes una app para gestionar contactos, cada contacto tiene un nombre y un número de teléfono, si el contacto tiene un número de teléfono válido (11 dígitos incluyendo el código de país) y un nombre valido se guarda en la lista de contactos y muestra el mensaje Contacto guardado, caso contrario se muestra el mensaje de error Datos incorrectos")

telefono = input("Ingrese su teléfono: ")
nombre = input("Ingrese su nombre: ")
valida_telefono=len(telefono) == 11

if valida_telefono and nombre:
    print("Contacto guardado")
else:        
    print("Datos incorrectos")
