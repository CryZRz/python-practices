class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def get_area(self):
        return self.base * self.altura


rectangulo : Rectangulo = Rectangulo(10, 5)
area = rectangulo.get_area()
print(area)