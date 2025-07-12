print("Crea un diccionario de alimentos y que animales domésticos lo consumen")
alimentos = {
    "carne": ["gato", "perro"],
    "zanahoria": ["conejo"]
}
print("Diccionario original: ", alimentos)
alimentos.update(
    pescado=["gato", "foca"],
    semillas=["pájaro", "hamster"],
    hierba=["vaca", "oveja"],
    trigo=["pájaro", "vaca"]
)
print("Añade al diccionario 4 alimentos más: ", alimentos)
existe_trigo = 'trigo' in alimentos
print("¿Existe trigo?", existe_trigo)
alimentos.pop("zanahoria")
print("Elimina zanahoria: ", alimentos)
