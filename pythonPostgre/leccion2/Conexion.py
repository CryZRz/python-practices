import psycopg2
from logger_base import log
import sys

class Conexion:
    _DATABASE = "test_python"
    _USERNAME = "postgres"
    _PASSWORD = "ps2746"
    _DB_PORT = 5433
    _HOST = "127.0.0.1"
    _conexion = None
    _cursor = None

    @classmethod
    def obteberConexion(cls):
        if cls._conexion == None:
            try:
                cls._conexion = psycopg2.connect(
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f"conexion exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.error(f"Ocurio una excepcion {e}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obteberConexion().cursor()
                log.debug(f"se abrio correctamente el cursor: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error("Ocurio una excepcion")
                sys.exit()
        else:
            return cls._cursor

if __name__ == "__main__":
    Conexion.obteberConexion()
    Conexion.obtenerCursor()