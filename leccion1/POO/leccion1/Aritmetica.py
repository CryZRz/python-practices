class Aritmetica:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def suma(self):
        return self.x + self.y

    def resta(self):
        return self.x - self.y

    def multplicar(self):
        return self.x * self.y

    def dividir(self):
        return self.x / self.y


operaciones: Aritmetica = Aritmetica(5, 10)
suma = operaciones.suma()
resta = operaciones.resta()
multiplicar = operaciones.multplicar()
dividir = operaciones.dividir()
print(suma)
print(resta)
print(multiplicar)
print(dividir)
