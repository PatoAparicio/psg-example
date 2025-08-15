print("Jhon y Jess coleccionan autos a escala 1:64.")
autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
if autos_jhon & autos_jess:
    print("Sí tienen autos en común")
    autos_comunes = autos_jhon & autos_jess
    print("Los autos en común son:", autos_comunes)
else:
    print("No tienen autos en común")