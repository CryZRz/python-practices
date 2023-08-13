from psycopg2 import pool
from logger_base import log
import sys

class Conexion:
    _DATABASE = "test_python"
    _USERNAME = "postgres"
    _PASSWORD = "ps2746"
    _DB_PORT = 5433
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f"creacion del pool exitoso {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"ocurrio un error al obtener el pool{e}")
                sys.exit()
        else:
            return cls._pool
    @classmethod
    def obteberConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"conexion obtenida del pool {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"regresamos la conexion al pool: {conexion}")

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()

if __name__ == "__main__":
    conexion = Conexion.obteberConexion()
    Conexion.obteberConexion()
    Conexion.liberarConexion(conexion)