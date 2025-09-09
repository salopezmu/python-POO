class perro:
    
    #atributos
    def __init__(self,edad,nombre,colorOjos):
        perro.edad =edad
        perro.nombre =nombre
        perro.colorOjos= colorOjos

    #metodos
    def pasear(self):
        print(f"el perro {perro.nombre} mueve la cola de alegria")

    def comer(self):
        print(f"el perro {perro.nombre} mueve la cola de alegria")

    def acariciar(self):
        print(f"el perro {perro.nombre} mueve la cola de alegria")

age= input("ingrese la edad de su perro:\n")
name= input("ingrese el nombre de su perro:\n")
colorEyes= input("ingrese el color de ojos de su perro:\n")
miperro= perro(age,name,colorEyes)

miperro.pasear()