cesta = ['🍑','🍓','🍉']
print (cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print (resultado)
print (cesta)
# Entrada de datos
sexo = input("Sexo (hombre/mujer): ").lower()
edad = int(input("Edad (años): "))
hemoglobina = float(input("Nivel de hemoglobina (g/dL): "))

# Determinamos si es niño (0-12) o adulto (13+)
es_nino = (edad <= 12)

# Calculamos los umbrales de anemia para cada caso
umbral_hombre = 13.5
umbral_mujer = 12.0
umbral_nino = 11.0

# Seleccionamos el umbral correcto usando operaciones lógicas
umbral = (
    (sexo == "hombre") * (not es_nino) * umbral_hombre +
    (sexo == "mujer") * (not es_nino) * umbral_mujer +
    es_nino * umbral_nino
)

# Evaluamos si hay anemia usando comparación directa
resultado = ("Anemia", "No Anemia")[hemoglobina >= umbral]

# Mostramos el resultado
print(resultado)