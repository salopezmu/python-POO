#los ciclos requieren minimo una linea de cogido en su interior
#el elif sirve para dar una jerarquia, para que si se ejecuta el primero no pregunte a los demas
#50000 5% 80000 8% 100000 10%
#siempre poner los ejercicion es bloques(funciones)
#las clases tienen unas caracteristicas y se las asignana un objeto (ej class bool asigna los valores de true/false a las variables)
#if_name_=="_main_":
#print(type(variable),variable)      para poder ver que tipo es la variable (con el type)
#ej booleano = "1" == 1 es tipo bool pq hace una comparacion y eso tiene mas jerarquia (se podria ver mejor como booleano = ("1" == 1))
def descuento():
    num = int(input("ingrese el valor de su compra en numeros enteros: "))
    descuento = 0
    if(num > 50000):
        descuento= 5
        compra=num-(num*(descuento/100))
    elif(num > 80000):
        descuento= 8
        compra=num-(num*(descuento/100))
    elif(num > 100000):
        descuento= 10
        compra=num-(num*(descuento/100))
    else: 
        descuento= 0
        compra=num*1
    print(f"su descuento es del {descuento}%, el valor de su compra es de: {compra}")
#esto se hace para en caso de tener codigo mas grande se pueda comentarear loq no queremos correr
def encuesta():
    for i in range(1,7):
        nombre = input("ingrese su nombre: ")
        carrera = input("ingrese su carrera: ")
        iproyecto = input("ingrese su idea de proyecto: ")
        print(f"{nombre} de la carrera {carrera} tiene la siguiente idea de proyecto: {iproyecto}")
encuesta()
def main():
    #descuento()
    encuesta()
#if _name_=="_main_":
#    main()
#1 byte = 8 bits; los bits se cuentan de derecha a izquierda
#diseñar una encuesta para 6 personas, obtener el nombre, carrera y idea de proyecto e imprimirlos en consola (subir a github)