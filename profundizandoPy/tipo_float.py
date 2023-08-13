#profundizando en el tipo float
a = 3.5

#Contructor de tipo flotante puede recibir int y str
a = float(10)
a = float("10")

#Notacion exponnecial (valores positivos o negativos)
a = 3e5
a = 3e-5
print(f"a: {a}")
#cualquer calculo que involucre un float, se promueve el float
a = 4.0 + 5
print(a)
print(type(a))