
import string

name = string
lastname = string

# valida nombre y apellido
name = input("What is your name?: ")

if name == "Alvaro":
        lastname = input("What is your last name?: ")
        if lastname == "Velueta":
            print("Great!!..You are Alvaro Velueta")
        else:
            print("Sorry!!!...YOU are NOT Alvaro Velueta !!!")
else:
    print ( "Sorry!!!...YOU are NOT Alvaro !!!"),
input("")
