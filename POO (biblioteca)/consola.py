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

biblioteca = Biblioteca(libros.copy(),3500)
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
    print("Libro agregado")
    print()

def actualizarExistencias():
    ISBN = input("ISBN del libro: ")
    esta = False
    for libro in biblioteca.getLibros():
        if libro.getISBN() == ISBN:
            esta = True
    if not esta:
        print("El libro no se encuentra en el inventario")
    else:
        accion = input("¿Añadir o quitar? ")
        if accion.lower() == "añadir":
            libro = biblioteca.buscarLibro(ISBN)
            biblioteca.buscarLibro(ISBN)
            cantidad = int(input("Cantidad: "))
            biblioteca.actualizarExistenciasLibro(cantidad,biblioteca.getLibros()[libro])
            print()
            print("Existencias actualizadas")
            print()
        elif accion.lower() == "quitar":
            libro = biblioteca.buscarLibro(ISBN)
            cantidad = -int(input("Cantidad: "))
            biblioteca.actualizarExistenciasLibro(cantidad,biblioteca.getLibros()[libro])
            print()
            print("Existencias actualizadas")
            print()
        else:
            print("Acción no indicada")

def realizarPrestamo():
    cedula = input("Cédula: ")
    cedulaEsta = False
    for cliente in biblioteca.getClientes():
        if cliente.getCedula() == cedula:
            cedulaEsta = True
    if not cedulaEsta:
        print("Cliente no registrado")
        return
    ISBN = input("ISBN del libro: ")
    esta = False
    for libro in biblioteca.getLibros():
        if libro.getISBN() == ISBN:
            esta = True
    if not esta:
        print("El libro no se encuentra en el inventario")
        return
    biblioteca.realizarPrestamo(ISBN,cedula)
    print()
    print("Prestamo realizado")
    print()

def registrarCliente():
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    biblioteca.registrarCliente(cedula,nombre,correo,direccion,telefono)
    print()
    print("Cliente registrado")
    print()

def devolverLibro():
    cedula = input("Cédula: ")
    devolucion = biblioteca.devolverLibro(cedula)
    if type(devolucion) == str:
        print("No se encontró un prestamo para el cliente indicado")
    else:
        print()
        print("Libro devuelto")
        print()

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
    elif accion == "3":
        realizarPrestamo()
    elif accion == "4":
        registrarCliente()
    elif accion == "5":
        devolverLibro()

    repetir = ""
    while repetir != "si" and repetir != "no":
        repetir = input("¿Desea continuar? ").lower()
        if repetir == "si":
            menu()
        elif repetir == "no":
            print("Gracias por usar la biblioteca")
            break

menu()