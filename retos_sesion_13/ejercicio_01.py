print("Imprimir los 20 primeros números de la sucesión de Lucas")
a= 2
b= 1
count=1
print(a)
print(b)
while (count<=18):
    c = a + b
    print(c)
    a = b  
    b = c
    count=count+1