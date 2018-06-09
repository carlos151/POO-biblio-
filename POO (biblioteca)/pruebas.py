from clases import *

#Biblioteca
autor1 = Autor("Antonio Recio","Español","21/05/1978")
autor2 = Autor("Manuel Murillo","Colombiano","04/04/1980")
autor3 = Autor("Pedro García","Mexicano","15/07/1960")

autores = [autor1,autor2,autor3]

libro1 = Libro("2010","Fake Editorial","3",7,"9345",["matemática","ciencia"],"Matemática en la Ciencia",autor1,0)
libro2 = Libro("2012","Not Fake Editorial","1",4,"4323",["matemática","cocina"],"Matemática en la Cocina",autor1,0)
libro3 = Libro("2016","Fake Editorial","1",2,"7435",["niños","cocina"],"Cocina para niños",autor2,0)
libro4 = Libro("2008","Fake Editorial 2.0","6",9,"3278",["niños","commputación"],"Computación para niños",autor3,0)

libros = [libro1,libro2,libro3,libro4]

biblioteca = Biblioteca(libros.copy(),3500,autores)


