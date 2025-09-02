
num= float(input("ingrese un numero de forma numerica:\n"))
suma=0
for i in range(num,num+101,1):
    suma+=i
print(f"la suma de los siguientes 100 numeros contando el {num} es {suma}")