import clases
import paises
import calendario
import calendar
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class RegistrarAutor:
    def __init__(self,root):
        self.__root = root
        root.title("Registrar Autor")
        root.minsize(height=500,width=500)
        root.resizable(height=False,width=False)

        self.__titleLabel = Label(root,text="Registrar Autor",font=("Arial","16"))
        self.__titleLabel.place(x=175,y=20)

        self.__nombreLabel = Label(root,text="Nombre:",font=("Arial","12"))
        self.__idLabel = Label(root,text="ID:",font=("Arial","12"))
        self.__fechaLabel = Label(root,text="Fecha de nacimiento:",font=("Arial","12"))
        self.__nacionalidadLabel = Label(root,text="Nacionalidad:",font=("Arial","12"))
        self.__nombreLabel.place(x=10,y=80)
        self.__idLabel.place(x=10,y=120)
        self.__fechaLabel.place(x=10,y=160)
        self.__nacionalidadLabel.place(x=10,y=200)

        self.__nombreEntry = Entry(root,width=50)
        self.__nombreEntry.place(x=80,y=81)

        self.__idEntry = Entry(root,width=50)
        self.__idEntry.place(x=80,y=121)

        self.__fechaEntry = calendario.Datepicker(self.__root,39)
        self.__fechaEntry.place(x=170,y=161)
        self.__calOriginal = Image.open("res/calendar.png")
        self.__calResized = self.__calOriginal.resize((20, 20), Image.ANTIALIAS)
        self.__cal = ImageTk.PhotoImage(self.__calResized)

        self.__nacionalidadEntry = Entry(root,width=42)
        self.__nacionalidadEntry.place(x=115,y=200)
        self.__arrowOriginal = Image.open("res/down_arrow.png")
        self.__arrowResized = self.__arrowOriginal.resize((20,20), Image.ANTIALIAS)
        self.__arrow = ImageTk.PhotoImage(self.__arrowResized)
        self.__nacionalidadBoton = Button(root,image=self.__arrow,font=("Arial","12"),height=20,width=20,command=self.abrirLista)
        self.__nacionalidadBoton.place(x=460,y=198)

        self.__nacionalidadLista = Listbox(root,font=("Arial","12"),height=11,width=37,selectmode=SINGLE)
        self.__nacionalidadLista.bind('<<ListboxSelect>>', self.onSelect)
        self.generarNacionalidades()

        self.__aceptar = Button(root,text="Aceptar",font=("Arial","12"),command=lambda: self.aceptar())
        self.__cancelar = Button(root,text="Cancelar",font=("Arial","12"),command=lambda: self.cancelar())
        self.__aceptar.place(x=85,y=450)
        self.__cancelar.place(x=320,y=450)

    def aceptar(self):
        #falta rellenar esto
        print("Hola mundo")

    def cancelar(self):
        self.__root.destroy()

    def onSelect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.__nacionalidadEntry.delete(0,END)
        self.__nacionalidadEntry.insert(0,value)


    def abrirLista(self):
        self.__nacionalidadLista.place(x=115, y=221)
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
            año = separarElementos[0]
            mes = separarElementos[1]
            dia = separarElementos[2]
            return dia + "/" + mes + "/" + año
        except:
            return ""

    def getNacionalidad(self):
        return self.__nacionalidadEntry.get()


ventana = Tk()
app = RegistrarAutor(ventana)
ventana.mainloop()

