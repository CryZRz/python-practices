#profundizando en tipo str
from mi_clase import MiClase

#help(MiClase)
#print(MiClase.__doc__)
print(MiClase.__init__.__doc__)

tupla_str = ("hola", "mundo", "universidad", "python")
mensaje = " ".join(tupla_str)
print(mensaje)

lista_cursos = ["Java", "python", "c++", "c#"]
mensaje = ", ".join(lista_cursos)
print(mensaje)

#metodo split
cursos = "Java Python Javascript c++"
lista_cursos2 = cursos.split()
#print(lista_cursos2)

cursos_coma = "Java,Python,Javascript,c++"
lista_cursos2 = cursos_coma.split(",")
print(lista_cursos2)

#dar formato a un str
nombre = "Christian"
edad = 19
sueldo = 3000
mensaje_con_formato = "Mi nombre es %s y tengo %d años"%(nombre, edad)
print(mensaje_con_formato)

mensaje_con_formato2 = "Nombre {} Edad {} Sueldo {:.2f}".format(nombre, edad, sueldo)
print(mensaje_con_formato2)

caracter_en_bytes = b"hola mundo"
print(caracter_en_bytes)
mensaje3 = b"Universidad python"
print(mensaje3[0])
print(chr(mensaje3[0]))

#convertir de str a bytes
string_nombre ="programación con python"
print("string original", string_nombre)
bytes = string_nombre.encode("UTF-8")
print("bytes codificados", bytes)

#covertir bytes a string
string2_nombre = bytes.decode("UTF-8")
print("string decodificado", string2_nombre)
print(string_nombre == string2_nombre)
