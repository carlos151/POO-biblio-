from clases import *
import paises
import calendario
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

#Biblioteca
autor1 = Autor("0010","Antonio Recio","Spain","21/05/1978")
autor2 = Autor("0154","Manuel Murillo","Colombia","04/04/1980")
autor3 = Autor("0576","Pedro García","Mexico","15/07/1960")

autores = [autor1,autor2,autor3]

direccion = Direccion("Rusia","Provincia1","Cantón1","Distrito1","Señas1")
lector1 = Cliente("3242","Chuck","Norris","Ortiz","carlos1512000@gmail.com",direccion,"84697598","res/ChuckNorris.png")

lectores = [lector1]

libro1 = Libro("2010","Fake Editorial","3",7,"9345",["matemática","ciencia"],"Matemática en la Ciencia",autor1,0)
libro2 = Libro("2012","Not Fake Editorial","1",4,"4323",["matemática","cocina"],"Matemática en la Cocina",autor1,0)
libro3 = Libro("2016","Fake Editorial","1",2,"7435",["niños","cocina"],"Cocina para niños",autor2,0)
libro4 = Libro("2008","Fake Editorial 2.0","6",9,"3278",["niños","commputación"],"Computación para niños",autor3,0)

libros = [libro1,libro2,libro3,libro4]

biblioteca = Biblioteca(libros.copy(),autores,lectores)


class Main: #Ventana principal
    def __init__(self,root):
        self.__root = root
        self.__root.config(bg="white")
        self.__root.title("Biblioteca")
        self.__root.minsize(height=500, width=500)
        self.__root.resizable(height=False, width=False)

        #textos
        self.__titleLabel = Label(root, bg="white", text="Bienvenido a la Biblioteca", font=("Helvetica", "16"))
        self.__titleLabel.place(x=127, y=40)
        self.__subtitleLabel = Label(root, bg="white", text="¿Qué desea hacer?", font=("Arial", "12"))
        self.__subtitleLabel.place(x=175, y=90)

        #Botones
        self.__nAutorBoton = Button(self.__root,bg="white",text="Registrar Autor",width=30,relief=RIDGE,bd=1,command=lambda: self.registrarAutor())
        self.__nAutorBoton.place(x=137,y=140)
        self.__nLibroBoton = Button(self.__root, bg="white",text="Registrar Libro", width=30, relief=RIDGE, bd=1)
        self.__nLibroBoton.place(x=137, y=170)
        self.__nClienteBoton = Button(self.__root, bg="white",text="Registrar Lector", width=30, relief=RIDGE, bd=1)
        self.__nClienteBoton.place(x=137, y=200)
        self.__buscarLibrosBoton = Button(self.__root, bg="white",text="Buscar Libros", width=30, relief=RIDGE, bd=1)
        self.__buscarLibrosBoton.place(x=137, y=230)
        self.__disponibleISBNBoton = Button(self.__root, bg="white",text="Consultar disponibilidad", width=30, relief=RIDGE, bd=1)
        self.__disponibleISBNBoton.place(x=137, y=260)
        self.__eliminarISBNBoton = Button(self.__root, bg="white",text="Eliminar Libro", width=30, relief=RIDGE, bd=1)
        self.__eliminarISBNBoton.place(x=137, y=290)
        self.__infoLectorBoton = Button(self.__root, bg="white",text="Consultar Información de Lector", width=30, relief=RIDGE, bd=1,command=lambda : self.consultarInfoLector())
        self.__infoLectorBoton.place(x=137, y=320)
        self.__prestamoBoton = Button(self.__root, bg="white",text="Realizar Préstamo", width=30, relief=RIDGE, bd=1)
        self.__prestamoBoton.place(x=137, y=350)
        self.__devolverBoton = Button(self.__root, bg="white",text="Realizar Devolución", width=30, relief=RIDGE, bd=1)
        self.__devolverBoton.place(x=137, y=380)
        self.__recordatorioBoton = Button(self.__root, bg="white",text="Enviar Recordatorio Masivo", width=30, relief=RIDGE, bd=1,command=lambda: self.enviarRecordatorio())
        self.__recordatorioBoton.place(x=137, y=410)

    def registrarAutor(self):
        ventana = Toplevel()
        app = RegistrarAutor(ventana)
        ventana.mainloop()

    def consultarInfoLector(self):
        ventana = Toplevel()
        app = InfoLector(ventana)
        ventana.mainloop()

    def enviarRecordatorio(self):
        biblioteca.enviarRecordatorio()
        messagebox.showinfo("Éxito","Recordatorios enviados")


class RegistrarAutor:
    def __init__(self,root):
        self.__root = root
        self.__root.config(bg="white")
        root.title("Registrar Autor")
        root.minsize(height=500,width=500)
        root.resizable(height=False,width=False)
        self.__canvas = Canvas(root,bg="#efefef",width=500,height=70).pack(side=TOP)

        self.__titleLabel = Label(root,bg="#efefef",text="Registrar Autor",font=("Helvetica","16"))
        self.__titleLabel.place(x=175,y=20)

        self.__nombreLabel = Label(root,bg="white",text="Nombre:",font=("Arial","12"))
        self.__idLabel = Label(root,bg="white",text="ID:",font=("Arial","12"))
        self.__fechaLabel = Label(root,bg="white",text="Fecha de nacimiento:",font=("Arial","12"))
        self.__nacionalidadLabel = Label(root,bg="white",text="Nacionalidad:",font=("Arial","12"))
        self.__nombreLabel.place(x=10,y=80)
        self.__idLabel.place(x=10,y=120)
        self.__fechaLabel.place(x=10,y=160)
        self.__nacionalidadLabel.place(x=10,y=200)

        self.__nombreEntry = ttk.Entry(root,width=67)
        self.__nombreEntry.place(x=80,y=81)

        self.__idEntry = ttk.Entry(root,width=67)
        self.__idEntry.place(x=80,y=121)

        self.__fechaEntry = calendario.Datepicker(self.__root,52)
        self.__fechaEntry.place(x=170,y=161)


        self.__nacionalidadEntry = ttk.Entry(root,width=56)
        self.__nacionalidadEntry.place(x=115,y=200)
        self.__arrowOriginal = Image.open("res/down_arrow.png")
        self.__arrowResized = self.__arrowOriginal.resize((20,20), Image.ANTIALIAS)
        self.__arrow = ImageTk.PhotoImage(self.__arrowResized)
        self.__nacionalidadBoton = Button(root,bg="white",bd=0,image=self.__arrow,command=self.abrirLista,activebackground="white")
        self.__nacionalidadBoton.place(x=460,y=200)

        self.__nacionalidadLista = Listbox(root,font=("Arial","12"),height=11,selectmode=SINGLE)
        self.__nacionalidadLista.bind('<<ListboxSelect>>', self.onSelect)
        self.generarNacionalidades()

        self.__aceptar = Button(root,bd=1,bg="white",font=("Arial","12"),relief=RIDGE,text="Aceptar",width=10,command=lambda: self.aceptar(),activebackground="white")
        self.__cancelar = Button(root,bg="white",font=("Arial","12"),relief=RIDGE,text="Cancelar",width=10,command=lambda: self.__root.destroy(),bd=1,activebackground="white")
        self.__aceptar.place(x=90,y=450)
        self.__cancelar.place(x=300,y=450)

    def _revisarFecha(self,fecha):
        day = fecha[:2]
        month = fecha[3:5]
        year = fecha[6:]
        try:
            dayAux = int(day)
            monthAux = int(month)
            yearAux = int(year)

        except:
            return False

        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            return False
        elif fecha[2] != "/" or fecha[5] != "/":
            return False
        else:
            return True

    def autorRepetido(self,id,nombre,nacionalidad,fecha):
        for autor in biblioteca.getAutores():
            print(autor.getNombre(),nombre)
            print(autor.getID(),id)
            print(autor.getNacionalidad(),nacionalidad)
            print(autor.getFechaNacimiento(),fecha)
            print()
            if autor.getID() == id and autor.getNombre() == nombre and autor.getNacionalidad() == nacionalidad and autor.getFechaNacimiento() == fecha:
                return True
        return False

    def aceptar(self):
        #falta rellenar esto
        id = self.getID()
        nombre = self.getNombre()
        nacionalidad = self.getNacionalidad()
        fecha = self.getFecha()

        if id == "" or nombre == "" or nacionalidad == "" or fecha == "":
            messagebox.showinfo("Error","No puede haber nada en blanco")
        elif not nacionalidad in paises.extraerPaises():
            messagebox.showinfo("Error","Selecciones una nacionalidad de la lista")
        elif not self._revisarFecha(fecha):
            messagebox.showinfo("Error","Debe elegir una fecha con el calendario")
        else:
            if self.autorRepetido(id,nombre,nacionalidad,fecha):
                messagebox.showinfo("Error", "Ese autor ya existe")
            else:
                biblioteca.registrarAutor(id,nombre,nacionalidad,fecha)
                self.__root.destroy()

    def onSelect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.__nacionalidadEntry.delete(0,END)
        self.__nacionalidadEntry.insert(0,value)


    def abrirLista(self):
        self.__nacionalidadLista.place(x=115, y=219,width=340)
        self.__nacionalidadBoton.configure(command=self.cerrarLista)

    def cerrarLista(self):
        self.__nacionalidadLista.place_forget()
        self.__nacionalidadBoton.configure(command=self.abrirLista)

    def generarNacionalidades(self):
        nacionalidades = paises.extraerPaises()
        nacionalidades.sort()
        for elemento in nacionalidades:
            self.__nacionalidadLista.insert(END,elemento)

    def getNombre(self):
        return self.__nombreEntry.get()

    def getID(self):
        return self.__idEntry.get()

    def getFecha(self):
        try:
            separarElementos = self.__fechaEntry.get().split("-")
            year = separarElementos[0]
            mes = separarElementos[1]
            dia = separarElementos[2]
            return dia + "/" + mes + "/" + year
        except:
            return self.__fechaEntry.get()

    def getNacionalidad(self):
        return self.__nacionalidadEntry.get()

class InfoLector:
    def __init__(self,root):
        self.__root = root
        self.__root.config(bg="white")
        root.title("Registrar Autor")
        root.minsize(height=500, width=400)
        root.resizable(height=False, width=False)

        self.__cedulaLabel = Label(self.__root,text="Cédula",bg="white").place(x=60,y=49)
        self.__cedulaEntry = Entry(self.__root,width=33,bg="white")
        self.__cedulaEntry.place(x=106,y=51)
        self.__buscar = Button(self.__root,text="Buscar",bg="white",bd=1,width=15,relief=RIDGE,command=lambda: self.buscar(self.__cedulaEntry.get()))
        self.__buscar.place(x=139,y=75)

    def buscar(self,cedula):
        for cliente in biblioteca.getClientes():
            if cliente.getCedula() == cedula:
                return self.mostrarInfo(cliente)
        messagebox.showerror("Error","Lector no encontrado")

    def mostrarInfo(self,cliente):
        for child in self.__root.winfo_children():
            child.destroy()
        img = Image.open(cliente.getFoto())
        resized = img.resize((150,200), Image.ANTIALIAS)
        foto = ImageTk.PhotoImage(resized)
        panel = Label(self.__root,image=foto,height=200,width=150)
        panel.image = foto
        panel.place(x=10,y=10)
        salir = Button(self.__root,text="Salir",width=15,relief=RIDGE,bd=1,bg="white",command=lambda: self.__root.destroy())
        salir.place(x=140,y=470)
        nombreCliente = cliente.getNombre() + " " + cliente.getApellido1() + " " + cliente.getApellido2()
        nombre = Label(self.__root,text="Nombre: " + nombreCliente,bg="white").place(x=175,y=10)
        correo = Label(self.__root,text="Correo: " + cliente.getCorreo(),bg="white").place(x=175,y=30)
        direccion = Button(self.__root,text="Dirección",width=15,relief=RIDGE,anchor="w",bd=0,bg="white",command=lambda:self.direccion(cliente.getDireccion()))
        direccion.place(x=175,y=50)
        telefono = Label(self.__root,text="Teléfono: " + cliente.getTelefono(),bg="white").place(x=175,y=70)
        prestamos = []
        for prestamo in cliente.getPrestamo():
            prestamos.append(prestamo)
        if prestamos == []:
            prestamos = "No tiene prestamos"
        prestamosLabel = Label(self.__root,text="Préstamos",bg="white").place(x=175,y=198)
        prestamosLista = Listbox(self.__root,width=63,height=15,bg="white")
        if type(prestamos) == list:
            for prestamo in prestamos:
                prestamosLista.insert(END,prestamo.getNombre())
            prestamosLista.bind('<<ListboxSelect>>', lambda: self.abrirPrestamo(prestamosLista.get(ACTIVE)))
            prestamosLista.bind('<MouseWheel>', lambda event, arg=prestamos: self.MouseWheel(event))
        else:
            prestamosLista.insert(END, prestamos)
        prestamosLista.place(x=10,y=220)


    def abrirPrestamo(self,prestamo):
        ventana = Tk()
        ventana.configure(bg="white")
        ventana.resizable(height=False, width=False)
        ventana.minsize(height=80, width=400)
        ventana.title("Prestamo: " + prestamo.getNombre())


    def MouseWheel(event, arg):  # Función para añadir la función de scroll
        for lista in arg:
            lista.yview("scroll", -(event.delta), "units")
        return "break"

    def direccion(self,direccion):
        ventana = Tk()
        ventana.configure(bg="white")
        ventana.resizable(height=False,width=False)
        ventana.minsize(height=80,width=400)
        ventana.title("Dirección")
        pais = "Pais: " + direccion.getPais()
        provincia = "Provincia: " + direccion.getProvincia()
        canton = "Cantón: " + direccion.getCanton()
        distrito = "Distrito: " + direccion.getDistrito()
        señas = "Señas: " + direccion.getSeñas()
        paisLabel = Label(ventana,text=pais,bg="white").place(x=15,y=10)
        provinciaLabel = Label(ventana,text=provincia,bg="white").place(x=15,y=30)
        cantonLabel = Label(ventana,text=canton,bg="white").place(x=15,y=50)
        distritoLabel = Label(ventana,text=distrito,bg="white").place(x=15,y=70)
        señasLabel = Label(ventana,text=canton,bg="white").place(x=15,y=90)
        cerrar = Button(ventana,text="Cerrar",width=15,relief=RIDGE,bd=1,bg="white",command=lambda: ventana.destroy()).place(x=140,y=160)
        ventana.mainloop()

#class RealizarPrestamo:







root = Tk()
app = Main(root)
root.mainloop()

