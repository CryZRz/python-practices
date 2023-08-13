from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("creacion objeto cuadrado".center(50, "*"))
cuadrado1 = Cuadrado(5, "verde")
print(cuadrado1.calcular_area())
print(Cuadrado.mro())

print("creacion objeto rectangulo".center(50, "*"))
rectangulo = Rectangulo(5, 9, "verde")
print(rectangulo)
print(rectangulo.calcular_area())
