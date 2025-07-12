print("El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que combine ambos estilos. Crea un conjunto con las prendas de ambos tipos con las listas de prendas:")
print('["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"] ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]')
conjunto_deportivo= {"Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"}
conjunto_formal= {"Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"}
union = conjunto_deportivo.union(conjunto_formal)
print("Conjunto de ropa: " , union)
