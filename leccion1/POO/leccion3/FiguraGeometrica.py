#ABC Abstract Base Class
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho: int, alto: int):
        if 0 < ancho < 10:
            self._ancho = ancho
        else:
            self._ancho = 0
        if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: int):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"valor erroneo en el ancho {self.ancho}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto: int):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"valor erroneo en el alto {self._alto}")

    def _validar_valor(self, valor: int):
        return 0 < valor < 10

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"alto: {self._alto} ancho: {self._ancho}"
