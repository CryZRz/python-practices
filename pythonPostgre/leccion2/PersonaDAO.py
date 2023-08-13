from Persona import Persona
from logger_base import log
from Conexion import Conexion
from cursor_del_pool import CursorDelPool


class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona ASC"
    _INSERTAR = "INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        # with Conexion.obtenerCursor() as cursor:

        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()

            personas: [Persona] = []

            for registgro in registros:
                persona = Persona(registgro[0], registgro[1], registgro[2], registgro[3])
                personas.append(persona.__str__())

            return personas

    @classmethod
    def insertar(cls, persona: Persona):
        #with Conexion.obteberConexion() as conexion:
            #with conexion.cursor() as cursor:
        with CursorDelPool() as cursor:
            log.debug(f"persona a insertar {persona}")

            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"persona a insertada {persona}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona: Persona):
        #with Conexion.obteberConexion() as conexion:
            #with conexion.cursor() as cursor:
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"persona actualizada : {persona}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona: Persona):
        #with Conexion.obteberConexion() as conexion:
            #with conexion.cursor() as cursor:
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"persona eliminada : {persona}")
            return cursor.rowcount


if __name__ == "__main__":
    # perosna = Persona(None, "Travis", "Scoot", "traviesoqmail.com")
    # persona_insert = PersonaDAO.insertar(persona=perosna)
    # log.debug(f"personas insertradas {persona_insert}")

    # actualizar persona
    # persona_update = Persona(11, "Abril", "Dzk", "dzkabril@gmail.com")
    # persona_updated = PersonaDAO.actualizar(persona_update)
    # log.debug(f"personas actualizada {persona_updated}")

    # eliminar persona
    persona_delete = Persona(id_persona=11)
    persona_deleted = PersonaDAO.eliminar(persona_delete)
    log.debug(f"personas eliminadas {persona_deleted}")

    # seleccionar personas
    personas = PersonaDAO.seleccionar()
    log.debug(personas)
