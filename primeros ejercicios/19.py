continuar=True
while (continuar==True):
    euro= float(input("ingrese su dinero en euros de forma numerica(ingrese un numero negativo para salir del programa): "))
    if euro>=0:
        print(f"su dinero en dolares corresponde a: {euro*1.17}")
    else:
        continuar=False