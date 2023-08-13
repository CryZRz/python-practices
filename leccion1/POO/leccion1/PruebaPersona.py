from Persona import Persona

def main():
    print("creacion de objetos".center(50, "-"))
    persona = Persona("Jimena", "Navarro", 18)
    persona.mostrar_detalle()

    persona2 = Persona("Chrstian", "Ramos", 19)
    # persona2.nombre = "Chris"
    # persona2.apellido = "remirez"
    persona2.mostrar_detalle()
    # Persona.mostrar_detalle(persona)
    persona2.telefono = "45896231"
    print(persona2.telefono)
    print(persona2.nombre)
    persona2.nombre = "Chris"
    print(persona2.mostrar_detalle())

    print("eliminacion de objetos".center(50, "-"))
    del persona2

if(__name__ == "__main__"):
    main()
