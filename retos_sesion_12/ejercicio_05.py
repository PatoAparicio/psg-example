print("Tienes una app para gestionar contactos, cada contacto tiene un nombre y un número de teléfono, si el contacto tiene un número de teléfono válido (11 dígitos incluyendo el código de país) y un nombre valido se guarda en la lista de contactos y muestra el mensaje Contacto guardado, caso contrario se muestra el mensaje de error Datos incorrectos")
contactos = []
telefono = input("Ingrese su teléfono: ")
nombre = input("Ingrese su nombre: ")
valida_telefono=len(telefono) == 11
valida_nombre = bool(nombre)
print("--------------------------------")
if valida_telefono and valida_nombre:
    contacto = {"nombre": nombre, "telefono": telefono}
    contactos.append(contacto)
    print("Contacto guardado")
else:        
    print("Datos incorrectos")

print("Lista de contactos:", list(contactos))