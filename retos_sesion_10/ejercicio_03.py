print("Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.")
print('Tienda Física: "Ana", "Luis", "Pedro", "María", "Juan"')
print('Tienda Online: "Pedro", "María", "Ana", "Carlos", "Laura"')
tienda_fisica = set(["Ana", "Luis", "Pedro", "María", "Juan"])
tienda_online = set(["Pedro", "María", "Ana", "Carlos", "Laura"])
ambos_canales = tienda_fisica & tienda_online
print("a. Clientes que compraron en ambos canales:", ambos_canales)
solo_fisica = tienda_fisica - tienda_online
print("b. Clientes que compraron solo en tienda física:", solo_fisica)
solo_online = tienda_online - tienda_fisica
print("c. Clientes que compraron solo online:", solo_online)