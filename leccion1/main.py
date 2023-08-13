#remember things of python
# hello world
print("hello world")

# variables
mumero = 15
cadena = "adwad"
flotante = 15.5
booleano = True

#posicion de memoria de varibles
pointer = id(mumero)
print(pointer)

#arrays
numbers_list = [1, 2, 3, 5, 4]
numbers_list.insert(0, 8)
func = lambda x, y : x*y
print(func(2, 20))
print(numbers_list)
numbers_list.pop()
del numbers_list[4]
print(numbers_list)

#sets
planetas = {"marte", "jupiter", "venus", "saturno"}
print(planetas)
print(len(planetas))
print("marte" in planetas)
planetas.add("tierra")
print(planetas)
#dont support duplicate elements
planetas.add("tierra")
print(planetas)
#remove elements posibility throw a error
planetas.remove("tierra")
print(planetas)
#remove elements dont throw a eeror
planetas.discard("tierras")
planetas.clear()
print(planetas)
del planetas

#dictionarys
diccionario = {
    "IDE": "ITELL IDEA",
    "RUST": "Programing languaje",
    "dbms": "data base managment system"
}
print(diccionario)
print(len(diccionario))
print(diccionario["RUST"])
diccionario.get("RUST")
#modify element
diccionario["RUST"] = diccionario["RUST"].upper()
print(diccionario.get("RUST"))

#recorer elementos de un diccionario
for i in diccionario:
    print(i)

for termino, valor in diccionario.items():
    print(termino + " " + valor)

print(diccionario.items())

#argumentos variables
def listar_numeros(*numero):
    for i in numero:
        print(i)

listar_numeros("christian", "uriel", "andres")

#pasar pares clave valor
def listar_terminos(**keywars):
    for llave, valor in keywars.items():
        print(f'{llave}: {valor}')

listar_terminos(RUST = "Programing languajes", JVM = "Java virtual machine")