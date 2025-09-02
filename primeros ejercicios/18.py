
num= int(input("ingrese un numero de forma numerica entera:\n"))
suma=0
for i in range(num,num+100):
    suma+=i
print(f"la suma de los siguientes 100 numeros contando el {num} es {suma}")