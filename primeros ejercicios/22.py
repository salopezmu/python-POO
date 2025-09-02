num= int(input("ingrese un numero de forma numerica:\n"))
print(f"los numeros impares menores que {num} son:")
for i in range(num-1,0,-1):
    if (i%2==1):
        print (i)
