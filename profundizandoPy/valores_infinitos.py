#Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float("inf")
#print(infinito_positivo)
#print(f"Es infinito?: {math.isinf(infinito_positivo)}")

infinito_negativo = float("-inf")
#print(infinito_negativo)
#print(f"Es infinito?: {math.isinf(infinito_negativo)}")

#modulo math
infinito_positivo = math.inf
#print(infinito_positivo)
#print(f"Es infinito?: {math.isinf(infinito_positivo)}")

infinito_negativo = -math.inf
#print(infinito_negativo)
#print(f"Es infinito?: {math.isinf(infinito_negativo)}")

#modulo decimal
infinito_positivo = Decimal("infinity")
print(infinito_positivo)
print(f"Es infinito?: {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-infinity")
print(infinito_negativo)
print(f"Es infinito?: {math.isinf(infinito_negativo)}")