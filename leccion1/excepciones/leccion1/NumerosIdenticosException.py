class NumeroIdenticosException(Exception):
    def __init__(self, mensaje: str):
        self.message = mensaje