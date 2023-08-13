class Persona:
    def __init__(self, nombre : str, edad : int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"nombre: {self.nombre} edad: {self.edad}"


class Empleado(Persona):
    def __init__(self, nombre : str, edad : int, sueldo : int):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()} sueldo: {self.sueldo}"
