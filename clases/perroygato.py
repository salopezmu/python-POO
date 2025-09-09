class perro:
    def __init__(self,color):
        perro.ladrar=True
        perro.color= color
        if (perro.ladrar==True): print(f"el perro de color {color} ladra")

class gato:
    def __init__(self,color2):
        gato.maullar=True
        gato.color2= color2
        if (gato.maullar==True): print(f"el gato de color {color2} maulla")
perro("amarillo")
gato("negro")