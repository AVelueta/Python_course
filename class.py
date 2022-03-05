class Humano:
     def __init__(Self):
         Self.edad = 25
#        print ("soy un nuevo objeto")

     def hablar(self, mensaje):
         print (mensaje)


pedro = Humano()
raul = Humano()

print ("soy Pedro y tengo ", pedro.edad)
print ("Soy Raul y tengo ", raul.edad)

pedro.hablar ('Hola')
raul.hablar ('Hola, pedro!')
