print("Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. A continuación tienes los postres que han ido pidiendo en cada salida:")
print('Jane: "Lemon Pie, Brownie, Tarta de Manzana,Helado de Chocolate, Flan"')
print('Jhon: "Carrot Cake, Croissant de Chocolate, Lemon Pie, Tarta de Manzana, Pudding"')
jane = {"Lemon Pie", "Brownie", "Tarta de Manzana","Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate","Lemon Pie", "Tarta de Manzana", "Pudding"}
comunes = jane & jhon
total_comunes = len(comunes)
total_jane = len(jane)
porcentaje = (total_comunes / total_jane) * 100
compatibles = (porcentaje > 50) * "Sí" + (porcentaje <= 50) * "No"
print("Postres en común:", jane & jhon)
print(f"Porcentaje de coincidencia: {porcentaje}%")
print("¿Son compatibles?", compatibles)