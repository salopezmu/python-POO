#diseñar una encuesta para 6 personas, obtener el nombre, carrera y idea de proyecto e imprimirlos en consola (subir a github)
def encuesta():
    for i in range(1,7):
        nombre = input("ingrese su nombre: ")
        carrera = input("ingrese su carrera: ")
        iproyecto = input("ingrese su idea de proyecto: ")
        print(f"{nombre} de la carrera {carrera} tiene la siguiente idea de proyecto: {iproyecto}")
encuesta()