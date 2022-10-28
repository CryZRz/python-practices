#own modules
#thirdy party modules
#python modules

from datetime import timedelta
import datetime 

import fmath
from colorama import Fore, Style

print(datetime.date.today())
print(timedelta(minutes = 100))

print(fmath.add(10, 50))
print(fmath.substract(50, 30))

print(Fore.RED + "Hello world")