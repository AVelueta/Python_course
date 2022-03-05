from multiprocessing.connection import wait
from turtle import color


numbers_list = list((1, 2, 3, 4))
colors = ['red', 'green', 'blue']

#print(type(numbers_list))

# r = list(range(1, 100)) 
# print(r)

#print(colors[2])
# print(colors)
# colors[1] = 'yellow'
# print(colors)

# colors.append('violet')
# print(colors)

# agrega 2 elementos a la lista
# colors.extend(['violet', 'yellow'])
# print(colors)

colors.insert(-1, 'violet')

#colors.insert(len(colors), 'violet')
# ordena la lista de color en orden alfabetico
#colors.sort()
#print(colors)

colors.sort(reverse=True)
print(colors)
