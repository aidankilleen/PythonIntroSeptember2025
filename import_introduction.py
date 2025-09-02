# import_introduction.py
import random

r = random.randint(1, 10)

numbers = [1,2,3,4,5,6,7]
print (numbers)

random.shuffle(numbers)

print (numbers)
print (r)

(a, b, *others) = numbers

print (f"a={a} b={b}")
print (others)



