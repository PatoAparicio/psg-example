print("Crear una lista de personas con 10 nombres de personas")
lista=["Luis", "Pamela", "Giovanni", "Miriam", "Oscar", "Jose","Pablo","Ximena","Lilian","Ruben"]
print("Obtener una sub lista de 5 a 9 con saltos de 2 en 2")
sub_lista = lista[5:9:2]
print(sub_lista)
print("Buscar si existe el nombre José en la lista original")
print ("Jose" in lista)
print("Ordenar la sub lista alfabéticamente a-z")
lista.sort()
print (lista)
print("Ordenar la lista original alfabéticamente descendente z-a")
lista.sort(reverse=True)
print (lista)