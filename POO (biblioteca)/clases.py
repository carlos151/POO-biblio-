import datetime
import time
from datetime import date
import yagmail

class Autor:
    def __init__(self, id,nombre, nacionalidad, fechaNacimiento):
        self.__nombre = nombre
        self.__id = id
        self.__nacionalidad = nacionalidad
        self.__fechaNacimiento = fechaNacimiento

    # accesores
    def getNombre(self):
        return self.__nombre

    def getID(self):
        return self.__id

    def getNacionalidad(self):
        return self.__nacionalidad

    def getFechaNacimiento(self):
        return self.__fechaNacimiento


class Libro:
    def __init__(self, año, editorial, edicion, copias, ISBN, palabrasClave, titulo, autor,imagen):
        self.__año = año
        self.__editorial = editorial
        self.__edicion = edicion
        self.__copiasIniciales = copias
        self.__copias = copias
        self.__ISBN = ISBN
        self.__palabrasClave = palabrasClave
        self.__titulo = titulo
        self.__autor = autor
        self.__caratula = imagen

    def modificarCopias(self,cantidad):
        self.__copias += cantidad
        if self.__copias <= 0:
            self.__copias = 0

    #accesores
    def getAño(self):
        return self.__año
    def getEditorial(self):
        return self.__editorial
    def getEdicion(self):
        return self.__edicion
    def getCopiasIniciales(self):
        return self.__copiasIniciales
    def getCopias(self):
        return self.__copias
    def getISBN(self):
        return self.__ISBN
    def getPalabrasClave(self):
        return self.__palabrasClave
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor

class Direccion:
    def __init__(self,pais,provincia,canton,distrito,señas):
        self.__pais = pais
        self.__provincia = provincia
        self.__canton = canton
        self.__distrito = distrito
        self.__señas = señas

    #accesores
    def getPais(self):
        return self.__pais
    def getProvincia(self):
        return self.__provincia
    def getCanton(self):
        return self.__canton
    def getDistrito(self):
        return self.__distrito
    def getSeñas(self):
        return self.__señas

class Cliente:
    def __init__(self,cedula,nombre,pAppelido,sApellido,correo,direccion,telefono,image):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__pApellido = pAppelido
        self.__sApellido = sApellido
        self.__correo = correo
        self.__direccion = direccion
        self.__telefono = telefono
        self.__foto = image
        self.__prestamos = []

    def todoAlDia(self):
        for prestamo in self.__prestamos:
            if self.calcularDeuda(prestamo) > 0:
                return False
        return True

    def calcularDeuda(self,prestamo):
        diferencia = prestamo.getFechaEntrega() - date.today()
        if diferencia > 0:
            return diferencia * 500
        else:
            return 0

    def eliminarPrestamo(self,prestamo):
        self.__prestamos.remove(prestamo)

    def añadirPrestamo(self,prestamo):
        self.__prestamos.append(prestamo)

    #accesores
    def getCedula(self):
        return self.__cedula
    def getNombre(self):
        return self.__nombre
    def getApellido1(self):
        return self.__pApellido
    def getApellido2(self):
        return self.__sApellido
    def getCorreo(self):
        return self.__correo
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getFoto(self):
        return self.__foto
    def getPrestamo(self):
        return self.__prestamos

class Prestamo:
    def __init__(self,ISBN,cedula):
        self.__ISBN = ISBN
        self.__cedula = cedula
        self.__fechaPrestamo = date.today()
        self.__fechaEntrega = self.__fechaPrestamo + datetime.timedelta(days=15)

    def getNombre(self,biblioteca):
        libros = Biblioteca.getLibros(biblioteca)
        for libro in libros:
            if libro.getISBN() == self.__ISBN:
                return libro.getTitulo()

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
    def __init__(self,libros,autores,clientes=[]):
        self.__clientes = clientes
        self.__libros = libros
        self.__prestamos = []
        self.__autores = autores

        #usuario para enviar correos
        self.__correo = "tallerprogra1@gmail.com"
        self.__password = "pass123456"

    def ingresarLibro(self,libro):
        if not libro in self.__libros:
            self.__libros.append(libro)
        else:
            return "Ese libro ya existe"

    def actualizarExistenciasLibro(self,cantidad,libro):
        libro.modificarCopias(cantidad)

    def formatoFechas(self,fecha):
        separarElementos = fecha.split("-")
        year = separarElementos[0]
        mes = separarElementos[1]
        dia = separarElementos[2]
        return dia + "/" + mes + "/" + year

    def enviarCorreo(self,correo,contraseña,destino,asunto,mensaje):
        yag = yagmail.SMTP(correo, contraseña)
        yag.send(destino, asunto, mensaje)

    def realizarPrestamo(self,ISBN,cedula):
        if type(self.buscarCliente(cedula)) == str:
            return -1
        if self.__clientes[self.buscarCliente(cedula)].todoAlDia:
            try:
                indiceLibro = self.buscarLibro(ISBN)
                if self.getLibros()[indiceLibro].getCopias() > 0:
                    prestamo = Prestamo(ISBN,cedula)
                    self.__prestamos.append(prestamo)
                    self.__clientes[self.buscarCliente(cedula)].añadirPrestamo(prestamo)
                    self.__libros[indiceLibro].modificarCopias(-1)
                    pISBN = prestamo.getISBN()
                    pCedula = prestamo.getCedula()
                    pFecha =self.formatoFechas(str(prestamo.getFechaPrestamo()))
                    pEntrega =self.formatoFechas(str(prestamo.getFechaEntrega()))
                    mensaje = "ISBN: " + pISBN + "\n"
                    mensaje += "Cédula: " + pCedula + "\n"
                    mensaje += "Fecha del préstamo: " + pFecha + "\n"
                    mensaje += "Fecha de entrega: " + pEntrega
                    destino = self.__clientes[self.buscarCliente(cedula)].getCorreo()
                    try:
                        self.enviarCorreo(self.__correo,self.__password,destino,"Detalles de préstamo",mensaje)
                    except:
                        return 0

                else:
                    return 1
            except:
                return "Libro no encontrado"
        else:
            return False

    def enviarRecordatorio(self):
        for cliente in self.__clientes:
            if cliente.todoAlDia():
                if cliente.getPrestamo() != []:
                    for prestamo in cliente.getPrestamo():
                        if prestamo.getFechaEntrega() > date.today():
                            pISBN = prestamo.getISBN()
                            pCedula = prestamo.getCedula()
                            pFecha = self.formatoFechas(str(prestamo.getFechaPrestamo()))
                            pEntrega = self.formatoFechas(str(prestamo.getFechaEntrega()))
                            mensaje = "ISBN: " + pISBN + "\n"
                            mensaje += "Cédula: " + pCedula + "\n"
                            mensaje += "Fecha del préstamo: " + pFecha + "\n"
                            mensaje += "Fecha de entrega: " + pEntrega + "\n"
                            mensaje += "Monto: " + str(cliente.calcularDeuda(prestamo))
                            destino = self.__clientes[self.buscarCliente(cliente.getCedula())].getCorreo()
                            try:
                                self.enviarCorreo(self.__correo, self.__password, destino, "Detalles de préstamo", mensaje)
                            except:
                                return False
                        else:
                            continue
                else:
                    continue

    def registrarCliente(self,cedula,nombre,pApellido,sApellido,correo,direccion,telefono,foto):
        cliente = Cliente(cedula,nombre,pApellido,sApellido,correo,direccion,telefono,foto)
        self.__clientes.append(cliente)

    def buscarPrestamo(self,prestamo):
        for i in range(len(self.__prestamos)):
            if self.__prestamos[i].getCedula() == prestamo.getCedula():
                return i
        return "Prestamo no encontrado"

    def buscarLibro(self,ISBN):
        for i in range(len(self.__libros)):
            if self.__libros[i].getISBN() == ISBN:
                return i
        return "Libro no encontrado"

    def buscarCliente(self,cedula):
        for i in range(len(self.__clientes)):
            if self.__clientes[i].getCedula() == cedula:
                return i
        return "Cliente no encontrado"

    def devolverLibro(self,prestamo):
        indicePrestamo = self.buscarPrestamo(prestamo)
        if type(indicePrestamo) == int:
            #eliminar prestamo de la biblioteca
            prestamo = self.getPrestamos()[indicePrestamo]
            self.__prestamos.pop(indicePrestamo)
            indiceLibro = self.buscarLibro(prestamo.getISBN())
            self.__libros[indiceLibro].modificarCopias(1)
            #eliminar prestamo del cliente
            cedula = self.__prestamos[indicePrestamo].getCedula()
            indiceCliente = self.buscarCliente(cedula)
            deuda = self.__clientes[indiceCliente].calcularDeuda(self.__prestamos[indicePrestamo])
            return deuda

        else:
            return indicePrestamo

    def eliminarLibro(self,ISBN):
        libro = self.buscarLibro(ISBN)
        if libro.getCopiasIniciales <= libro.getCopias:
            self.__libros.remove(libro)
        else:
            return False

    def cosultarLibroISBN(self,ISBN):
        for libro in self.__libros:
            if libro.getISBN() == ISBN:
                return libro

    def consultarLibrosAutor(self,autor):
        libros = []

        for elemento in self.__libros:
            if elemento.getAutor().getNombre().lower() == autor.lower():
                if not elemento in libros:
                    libros.append(elemento.getNombre())
        return libros

    def consultarLibrosEditorial(self,editorial):
        libros = []

        for elemento in self.__libros:
            if elemento.getEditorial.lower() == editorial.lower():
                if not elemento in libros:
                    libros.append(elemento.getNombre())
        return libros

    def consultarLibrosPalabrasClave(self,palabras):
        libros = []

        for elemento in self.__libros:
            for palabra in palabras:
                for clave in elemento.getPalabrasClave():
                    if palabra.lower() == clave.lower():
                        if not elemento in libros:
                            libros.append(elemento.getNombre())
        return libros


    def consultarClientes(self,cedula):
        for cliente in self.__clientes:
            if cliente.getCedula() == cedula:
                return cliente

    def registrarAutor(self,nombre,id,nacionalidad,fechaNacimiento):
        autor = Autor(nombre,id,nacionalidad,fechaNacimiento)
        self.__autores.append(autor)


    #accesores
    def getClientes(self):
        return self.__clientes
    def getLibros(self):
        return self.__libros
    def getPrestamos(self):
        return self.__prestamos
    def getAutores(self):
        return self.__autores
