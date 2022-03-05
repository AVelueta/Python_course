
# function sample 1
#-----------------------------------
from ast import Add


def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 50))

# funtion sample 2

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(25, 50))
input("")