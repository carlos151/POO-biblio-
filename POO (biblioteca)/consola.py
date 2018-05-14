from clases import *


#Biblioteca
autor1 = Autor("0010","Antonio Recio","Español","21/05/1978")
autor2 = Autor("0154","Manuel Murillo","Colombiano","04/04/1980")
autor3 = Autor("0576","Pedro García","Mexicano","15/07/1960")

autores = [autor1,autor2,autor3]

libro1 = Libro("2010","Fake Editorial","3",7,"9345",["matemática","ciencia"],"Matemática en la Ciencia",autor1)
libro2 = Libro("2012","Not Fake Editorial","1",4,"4323",["matemática","cocina"],"Matemática en la Cocina",autor1)
libro3 = Libro("2016","Fake Editorial","1",2,"7435",["niños","cocina"],"Cocina para niños",autor2)
libro4 = Libro("2008","Fake Editorial 2.0","6",9,"3278",["niños","commputación"],"Computación para niños",autor3)

libros = [libro1,libro2,libro3,libro4]

biblioteca = Biblioteca(libros,3500)
#Biblioteca

def ingresarLibro():
    año = input("Año: ")
    editorial = input("Editorial: ")
    edicion = input("Edición: ")
    copias = int(input("Copias: "))
    ISBN = input("ISBN: ")
    palabrasClave = input("Palabras clave: ")
    palabrasClave.split(",")
    nombre = input("Nombre: ")
    id = input("ID del autor: ")
    autor = ""
    for a in autores:
        if a.getID() == id:
            autor = a
    if autor == "":
        print("El autor no está registrado, indique sus datos")
        print()
        nombreAutor = input("Nombre: ")
        nacionalidadAutor = input("Nacionalidad:")
        fechaAutor = input("Fecha de nacimiento: ")
        autor = Autor(id,nombreAutor,nacionalidadAutor,fechaAutor)
    libro = Libro(año,editorial,edicion,copias,ISBN,palabrasClave,nombre,autor)
    biblioteca.ingresarLibro(libro)
    print()
    print("Libro agregado con éxito")

def actualizarExistencias():
    ISBN = input("ISBN del libro: ")
    esta = False
    for libro in biblioteca.getLibros():
        if libro.getISBN() == ISBN:
            esta = True
    if not esta:
        print("El libro no se encuentra en el inventario")

    accion = input("¿Añadir o quitar")
    if accion.lower() == añadir:
        cantidad = int(input("Cantidad: "))
    elif accion.lower() == añadir:
        cantidad = -int(input("Cantidad: "))
    else:
        print("Acción no indicada")
        return
    biblioteca.actualizarExistenciasLibro()

def menu():
    print("Bienvenido a la biblioteca")
    print()
    print("1.Ingresar un libro")
    print("2.Actualizar existencias de un libro")
    print("3.Realizar un préstamo")
    print("4.Registrar un cliente")
    print("5.Devolver un libro")
    print("6.Buscar libros por autor")
    print("7.Buscar libros por palabras clave")
    print("8.Buscar cliente")
    print()
    accion = input("¿Qué desea hacer?")
    if accion == "1":
        ingresarLibro()
    elif accion == "2":
        actualizarExistencias()


menu()