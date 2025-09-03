# import_investigation4.py

# just import the function(s) or other resource(s) from the module
from random import randint, choice
import numpy as np

def randint(x, y):
    print ("this doesn't produce a random int")
    return 27


r = randint(1, 100)

print (r)

np.random.randint()


names = ['Alice', 'Bob', 'Carol', 'Dan']

chosen_name = choice(names)

print (chosen_name)


