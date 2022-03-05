# types of modules:
# 1) own modules
# 2) thirdy party modules
# 3) python modules
# tip: find in goggle pip modules > PyPI ( pypi.org)
# ----------------------------------

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))


# Second option from the library named "datetime"
# import only the method named "timedelta"
# -------------------------------------------

from datetime import timedelta
from datetime import date

print( timedelta(minutes=120))
print(date.today())


# use the library f_math
#------------------------------

import f_math

f_math.add(3, 10)
f_math.substract(3, 10)

# use library colorama from pypi.org
#-----------------------------------------
#from colorama import Fore, Style, init
#init(convert=True)
#print(fore.RED + "Hello world")