print('Crea una tupla con los siguientes elementos: a,b,c,d,e,f,g,h,i,j ')
tupla=('a','b','c','d','e','f','g','h','i','j')
print ("Primer elemento:", tupla[0])
print ("Último elemento:", tupla[-1])
sub_tupla_1 = tupla[2:5]
print ("Slice [3:5]:",sub_tupla_1 )
sub_tupla_2 = tupla[4:10:3]
print ("Slice [5:9:3]:",sub_tupla_2 )
sub_tupla_3 = tupla[9:0:-2]
print ("Slice [9:0:-2]:",sub_tupla_3 )
