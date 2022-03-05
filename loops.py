#sample for loops use with for - if
#------------------------------------------------------------------

foods = ['Apples', 'Bread', 'Cheese', 'Milk', 'Bananas', 'Graves']

for food in foods:
    if food == "Cheese":
        option = food
        print("You have to buy this: ", option )
        continue
    print(food)

#-----------------------------------------------------------------
# sample using for in range values
# ---------------------------------------------------------------
for number in range(1, 20):
    print(number)

#------------------------------------------------------------------
# sample using While
#----------------------------------------------------------------

count = 5

while count <= 10:
    print(count)
    count = count + 1