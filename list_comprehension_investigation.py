# list_comprehension_investigation.py


names = ["alice", "bob", "carol", "dan"]

# this is not the python way of doing things
capitalised_names = []

for name in names:
    capitalised_names.append(name.capitalize())

print (names)
print (capitalised_names)

# python way
# use a list comprehension
capitalised_names = [name.capitalize() for name in names]
print (capitalised_names)


# using list comprehension to filter a list

numbers = [1, 4, 2, 3, 5, 7, 10, 9]
even_numbers = [n for n in numbers if n % 2 == 0]

print (numbers)
print (even_numbers)

# using list comprehension to create combinations
colours = ["red", "green", "blue"]
products = ["pen", "pencil", "crayon"]

product_list = [ f"{colour} {product}" for colour in colours for product in products]
print (product_list)


# playing cards
# suit - H, S, D, C
# value - A, 2, 3, ..., 10, J, Q, K

# create an array with all playing cards AH -> KC

# (strings)

name = "Aidan"
name = 'Aidan'

name = "O'Sullivan"
message = 'press the "red" button'
message = "press the \"red\" button"
name = 'O\'Sullivan'


suits = ["H", "S", "D", "C"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards = [f"{value}{suit}" for suit in suits for value in values]

print (cards)

from random import shuffle

shuffle(cards)

print (cards)











































