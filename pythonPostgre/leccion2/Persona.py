class Persona:
    def __init__(self, id_persona: int | None = None, nombre: str | None = None, apellido: str | None = None, email: str | None = None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f"Persona idPersona: {self._id_persona} nombre {self._nombre} apellido {self._apellido} email: {self._email}"

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id: int | None):
        self._id_persona = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str | None):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str | None):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str | None):
        self._email = email
