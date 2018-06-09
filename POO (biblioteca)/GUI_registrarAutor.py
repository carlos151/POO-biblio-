from clases import *
import paises
import calendario
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
from datetime import date

#Biblioteca
autor1 = Autor("0010","Antonio Recio","Español","21/05/1978")
autor2 = Autor("0154","Manuel Murillo","Colombiano","04/04/1980")
autor3 = Autor("0576","Pedro García","Mexicano","15/07/1960")

autores = [autor1,autor2,autor3]

libro1 = Libro("2010","Fake Editorial","3",7,"9345",["matemática","ciencia"],"Matemática en la Ciencia",autor1,0)
libro2 = Libro("2012","Not Fake Editorial","1",4,"4323",["matemática","cocina"],"Matemática en la Cocina",autor1,0)
libro3 = Libro("2016","Fake Editorial","1",2,"7435",["niños","cocina"],"Cocina para niños",autor2,0)
libro4 = Libro("2008","Fake Editorial 2.0","6",9,"3278",["niños","commputación"],"Computación para niños",autor3,0)

libros = [libro1,libro2,libro3,libro4]

biblioteca = Biblioteca(libros.copy(),3500,autores)

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
        self.__cancelar = Button(root,bg="white",font=("Arial","12"),relief=RIDGE,text="Cancelar",width=10,command=lambda: self.cancelar(),bd=1,activebackground="white")
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
            autor = Autor(id,nombre,nacionalidad,fecha)
            biblioteca.registrarAutor(autor)


    def cancelar(self):
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




