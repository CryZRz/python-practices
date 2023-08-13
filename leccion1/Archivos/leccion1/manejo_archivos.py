try:
    archivo = open("prueba.txt", "w", encoding="utf-8")
    archivo.write("Valeria ")
    archivo.write("tkm")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("fin del archivo")