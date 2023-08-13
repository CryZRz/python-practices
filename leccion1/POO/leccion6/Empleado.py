class Empleado:
    def __init__(self, nombre: str, sueldo: int):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"empleado: {self.nombre} sueldo: {self.sueldo}"