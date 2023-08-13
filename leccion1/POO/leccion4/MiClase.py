class MiClase:
    variable_clase = "valor variable clase"

    def __init__(self, variable_instancia: str):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatic():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

print(MiClase.variable_clase)
mi_clase = MiClase("variable instancia")
print(mi_clase.variable_instancia)
print(mi_clase.variable_clase)

MiClase.variable_clase2 = "Valor varibale clase 2"

mi_clase2 = MiClase("otro valor de variable instancia")
print(mi_clase2.variable_instancia)
print(MiClase.variable_clase2)
print(mi_clase.variable_clase2)
print(mi_clase2.variable_clase2)
MiClase.metodo_estatic()
MiClase.metodo_clase()