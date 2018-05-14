import datetime
import time
from datetime import date

class Autor:
    def __init__(self,id, nombre, nacionalidad, fechaNacimiento):
        self.__id = id
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__fechaNacimiento = fechaNacimiento

    # accesores
    def getID(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getNacionalidad(self):
        return self.__nacionalidad

    def getFechaNacimiento(self):
        return self.__fechaNacimiento


class Libro:
    def __init__(self, año, editorial, edicion, copias, ISBN, palabrasClave, nombre, autor):
        self.__año = año
        self.__editorial = editorial
        self.__edicion = edicion
        self.__copias = copias
        self.__ISBN = ISBN
        self.__palabrasClave = palabrasClave
        self.__nombre = nombre
        self.__autor = autor

    def modificarCopias(self,cantidad):
        self.__copias += cantidad

    #accesores
    def getAño(self):
        return self.__año
    def getEditorial(self):
        return self.__editorial
    def getEdicion(self):
        return self.__edicion
    def getCopias(self):
        return self.__copias
    def getISBN(self):
        return self.__ISBN
    def getPalabrasClave(self):
        return self.__palabrasClave
    def getNombre(self):
        return self.__nombre
    def getAutor(self):
        return self.__autor

class Cliente:
    def __init__(self,cedula,nombre,correo,direccion,telefono):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__correo = correo
        self.__direccion = direccion
        self.__telefono = telefono
        self.__deudas = 0

    def modificarDeudas(self,cantidad):
        self.__deudas += cantidad

    #accesores
    def getCedula(self):
        return self.__cedula
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getDeudas(self):
        return self.__deudas

class Prestamo:
    def __init__(self,ISBN,cedula):
        self.__ISBN = ISBN
        self.__cedula = cedula
        self.__fechaPrestamo = date.today()
        self.__fechaEntrega = self.__fechaPrestamo + datetime.timedelta(days=15)

    #accesores
    def getISBN(self):
        return self.__ISBN
    def getCedula(self):
        return self.__cedula
    def getFechaPrestamo(self):
        return self.__fechaPrestamo
    def getFechaEntrega(self):
        return self.__fechaEntrega

class Biblioteca:
    def __init__(self,libros,deudas):
        self.__clientes = []
        self.__libros = libros
        self.__prestamos = []
        self.__deuda = deudas

    def ingresarLibro(self,libro):
        if not libro in self.__libros:
            self.__libros.append(libro)
        else:
            return "Ese libro ya existe"

    def actualizarExistenciasLibro(self,cantidad,libro):
        libro.modificarCopias(cantidad)

    def realizarPrestamo(self,ISBN,cedula):
        prestamo = Prestamo(ISBN,cedula)
        self.__prestamos.append(prestamo)
        indiceLibro = self.buscarLibro(prestamo.getISBN())
        self.__libros[indiceLibro].modificarCopias(-1)

    def registrarCliente(self,cedula,nombre,correo,direccion,telefono):
        cliente = Cliente(cedula,nombre,correo,direccion,telefono)
        self.__clientes.append(cliente)

    def buscarPrestamo(self,cedula):
        for i in range(len(self.__prestamos)):
            if self.__prestamos[i].getCedula() == cedula:
                return i
        return "Prestamo no encontrado"

    def buscarLibro(self,ISBM):
        for i in range(len(self.__libros)):
            if self.__libros[i].getISBN() == ISBM:
                return i
        return "Libro no encontrado"

    def buscarCliente(self,cedula):
        for i in range(len(self.__clientes)):
            if self.__clientes[i].getCedula() == cedula:
                return i
        return "Cliente no encontrado"

    def devolverLibro(self,cedula):
        indicePrestamo = self.buscarPrestamo(cedula)
        if type(indicePrestamo) == int:
            prestamo = self.getPrestamos()[indicePrestamo]
            if prestamo.getFechaEntrega() < date.today():
                cedula = self.__prestamos[indicePrestamo].getCedula()
                indiceCliente = self.buscarCliente(cedula)
                self.__clientes[indiceCliente].modificarDeudas(self.__deuda)
            self.__prestamos.pop(indicePrestamo)
            indiceLibro = self.buscarLibro(prestamo.getISBN())

            self.__libros[indiceLibro].modificarCopias(1)
        else:
            return indicePrestamo

    def consultarLibrosAutor(self,autor):
        libros = []

        for elemento in self.__libros:
            if elemento.getAutor().getNombre().lower() == autor.lower():
                if not elemento in libros:
                    libros.append(elemento)
        return libros

    def consultarLibrosPalabrasClave(self,palabras):
        libros = []

        for elemento in self.__libros:
            for palabra in palabras:
                for clave in elemento.getPalabrasClave():
                    if palabra.lower() == clave.lower():
                        if not elemento in libros:
                            libros.append(elemento)
        return libros


    def consultarClientes(self,cedula):
        for cliente in self.__clientes:
            if cliente.getCedula() == cedula:
                return cliente

    #accesores
    def getClientes(self):
        return self.__clientes
    def getLibros(self):
        return self.__libros
    def getPrestamos(self):
        return self.__prestamos