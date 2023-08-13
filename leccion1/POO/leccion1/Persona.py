class Persona:

    def __init__(self, nombre: str, apellido: str, edad: int, *args, **kwargs):
        self._nombre = nombre  # _varibale para encapsular
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"{self._nombre} {self._apellido} {self._edad}")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre : str):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        self._nombre = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        self._edad = edad

    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido} se ha borrado")
if(__name__ == "__main__"):
    persona = Persona("Jimena", "Navarro", 18)
    persona.mostrar_detalle()

    persona2 = Persona("Chrstian", "Ramos", 19)
    # persona2.nombre = "Chris"
    # persona2.apellido = "remirez"
    persona2.mostrar_detalle()
    # Persona.mostrar_detalle(persona)
    persona2.telefono = "45896231"
    print(persona2.telefono)
    print(persona2.nombre)
    persona2.nombre = "Chris"
    print(persona2.mostrar_detalle())