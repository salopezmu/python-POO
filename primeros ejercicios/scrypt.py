#Autor: Santiago López Murcia
#Esto es una prueba para novatos
#1
texto = int(input("escriba un numero del 1 al 10\n"))
print(f"el numero {texto} tiene la siguiente tabla de multiplicar (del 1 al 10)")

#2 realizar las tablas d multiplicar del numero q usted ingrese
count=0
for i in range(1,11):
    count+=1
    print(f"{count}. {texto*i}")

#3 utilizando una funcion obtenga el numero factorial de un numero dado
print(f"el factorial del numero {texto} es:")
def x(a):
    z=a
    for i in range(a-1,0,-1):
        z*=i
    return z
print(x(texto))