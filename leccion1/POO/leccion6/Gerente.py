from POO.leccion6.Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre: str, sueldo: int, departamento: str):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f"Gerente [Departamento: {self.departamento}] {super().__str__()}"