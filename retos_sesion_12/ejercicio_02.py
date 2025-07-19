print("Tienes una app para gestionar tareas de 4 usuarios, para acceder los usuarios deben iniciar sesión con un nombre de usuario y una contraseña introducidos por teclado. Define los siguientes usuarios y contraseñas utilizando la estructura de datos mas adecuada.")
usuarios = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'user123',
    'user3': 'user123'
}
nombre_usuario = input("Usuario: ")
contrasena = input("Contraseña: ")
if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado")