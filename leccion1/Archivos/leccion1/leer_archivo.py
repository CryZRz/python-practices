try:
    archivo = open("prueba.txt", "r", encoding="utf8")
    #print(archivo.read())

    #leer algunos caracteres
    #print(archivo.read(7))

    #leer lineas completas
    #print(archivo.readline())

    #iterar archivo
    #for linea in archivo:
    #    print(linea)

    #leer todas la lineas
    #print(archivo.readlines())

    #a anexar informacion
    archivo2 = open("copia.txt", "a")
    archivo2.write(archivo.read())
    print("se ha leido y copiado")
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()