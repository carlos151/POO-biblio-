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
        self.__root.config(bg="white")
        root.title("Registrar Autor")
        root.minsize(height=500,width=500)
        root.resizable(height=False,width=False)
        self.__canvas = Canvas(root,bg="#c1c1c1",width=500,height=70).pack(side=TOP)

        self.__titleLabel = Label(root,bg="#c1c1c1",text="Registrar Autor",font=("Helvetica","16"))
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
        self.__calOriginal = Image.open("res/calendar.png")
        self.__calResized = self.__calOriginal.resize((20, 20), Image.ANTIALIAS)
        self.__cal = ImageTk.PhotoImage(self.__calResized)

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
            return ""

    def getNacionalidad(self):
        return self.__nacionalidadEntry.get()


ventana = Tk()
app = RegistrarAutor(ventana)
ventana.mainloop()

