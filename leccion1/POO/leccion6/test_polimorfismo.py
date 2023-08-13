from Gerente import Gerente
from Empleado import Empleado


def imprimir_detalles(objecto: object):
    print(objecto)
    if isinstance(objecto, Gerente):
        print(objecto.departamento)
    print(type(objecto))

empleado = Empleado("Juan", 3000)
imprimir_detalles(empleado)
gerente = Gerente("Chrsitian", 4000, "jvm")
imprimir_detalles(gerente)