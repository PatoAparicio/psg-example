resto_1 = 44 % 2
resto_2 = 98 % 2
paridad_1=resto_1==0
paridad_2=resto_2==0
print ("44 y 98 tienen la misma paridad?", not ((paridad_1 or paridad_2) and not (paridad_1 and paridad_2)))
resto_3 = 111 % 2
resto_4 = 333 % 2
paridad_3=resto_3==0
paridad_4=resto_4==0
print ("111 y 333 tienen la misma paridad?", not ((paridad_3 or paridad_4) and not (paridad_3 and paridad_4)))