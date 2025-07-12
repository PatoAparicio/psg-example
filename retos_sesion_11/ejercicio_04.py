print("Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies")
habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}
habitats.update(
    sabana={
        "especies": {"león", "cebra"}
    },
    arrecife={
        "especies": {"tortuga marina", "pez payaso"}
    }
)
print("Añade al diccionario 2 habitats: ", habitats)
existe_amazonas = 'amazonas' in habitats
print("¿Existe amazonas?", existe_amazonas)
habitats["amazonas"]["especies"].add("anaconda")
print("Añade al amazonas la especie 'anaconda':", habitats)