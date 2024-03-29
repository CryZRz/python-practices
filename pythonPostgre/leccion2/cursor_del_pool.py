from logger_base import log
from ConexionPool import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__")
        self._conexion = Conexion.obteberConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug("Se ejecuta el metodo exit")
        if exc_val:
            self._conexion.rollback()
            log.error(f"ocurrio una excepcion: {exc_val} {exc_type} {exc_tb}")
        else:
            self._conexion.commit()
            log.debug("comit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())