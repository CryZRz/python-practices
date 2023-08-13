from NumerosIdenticosException import  NumeroIdenticosException

resultado = None

try:
    a = int(input("ingresa un numero"))
    b = int(input("ingresa otro numero"))
    if a == b:
        raise NumeroIdenticosException("numeros identicos")
    resultado = a/b
except ZeroDivisionError as e:
    print(f"ZeroDivisionError division entre 0 {e}")
except TypeError as e:
    print(f"TypeError Ocurrio un error {e}")
except Exception as e:
    print(f"Exception ocurrio un error {e}")
else:
    #solo se ejecuta cuando nose arroja una excpecion
    print("No se arrojo ninguna excepcion")
finally:
    print("valeria")

print("continuamos.....")