print ("Sistema de seguridad XOR")
tarjeta = True
huella = True
print ("Ambas activas: ", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = False
huella = True
print ("Solo huella activa: ", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = True
huella = False
print ("Solo tarjeta activa: ", (tarjeta or huella) and not (tarjeta and huella))
tarjeta = False
huella = False
print ("Ambos desactivos: ", (tarjeta or huella) and not (tarjeta and huella))
