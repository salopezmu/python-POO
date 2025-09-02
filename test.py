#Auntor: Santiago Lopez Murcia
#primera version
#1. estructuras de control
#if, for,while,switch,dowhile
#prueba
#estructura un programa que mencione si su calificacion es meritoria
#4.5  5 meritorio
#nota= float(input("escriba la nota en forma numerica entre 0 y 5: "))
#if (nota>=4.5):
#    print("esta nota es meritoria")
#else:
#    print("su nota no es meritoria")

#1 euro = 1.17 dolares
continuar=True
while(continuar==True):
    euro= float(input("ingrese su dinero en euros de forma numerica(ingrese un numero negativo para salir del programa): "))
    if euro<0:
        continuar=False
    else:
        print(f"su dinero en dolares corresponde a: {euro*1.17}")

