print('Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies: {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}')
arca = {
    "🐶": 2,
    "🐱": 2,
    "🐯": 2,
    "🐵": 2,
    "🦄": 0,
    "🦒": 1
}
arca.update({'🐍':'2','🦅':'2','🐘':'2'})
print("Añade al arca 3 especies: ", arca)
animales_arca = iter(arca.items())
print("Toma lista de los animales en el arca son: ")
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
siguiente = next(animales_arca) 
print(siguiente)
siguiente = next(animales_arca)
print(siguiente)
existe_dragon = '🐲' in arca
print("¿Existe dragón?", existe_dragon)
del arca["🦄"]
print("Elimina la especie unicornio del arca",arca)
arca["🦒"] = 2
arca.clear()
print("Arca después del diluvio:", arca)