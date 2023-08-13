#with open("prueba.txt", "r", encoding="utf8") as archivo:
#    print(archivo.read())

from Archivos.leccion1.ManejoArchivo import ManejoArchivo

with ManejoArchivo("prueba.txt") as archivo:
    print(archivo.read())