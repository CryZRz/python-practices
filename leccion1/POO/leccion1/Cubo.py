class Cubo:
    def __init__(self, *lados : int):
        self.lados = lados

    def get_volumen(self):
        volumen = 1
        for i in self.lados:
            volumen *= i

        return volumen


cubo : Cubo = Cubo(3, 5, 6)
print(cubo.get_volumen())