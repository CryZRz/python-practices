class Persona:
    contador_personas = 0

    @classmethod
    def increment(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre: str, edad: int):
        Persona.increment()
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"idpersona: {self.id_persona} nombre: {self.nombre} edad: {self.edad}"


persona = Persona("Jimena", 28)
print(persona)
persona2 = Persona("Christian", 28)
print(persona2)
persona3 = Persona("Jonathan", 28)
print(persona3)
print(Persona.contador_personas)