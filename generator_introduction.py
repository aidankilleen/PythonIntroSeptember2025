# generator_introduction.py

# a generator is a function that uses "yield" insted of "return"
# the thing that is iterating will call the generator for each item
# under the hood - generators are "lazy" and memory efficient

def get_number():
    print("get_number() called")
    numbers = [1, 4, 3, 2, 5, 10]

    for n in numbers:
        print (f"yielding {n}")
        yield n

# a generator is a function that creates an iterable
# we can iterate using a for loop
for n in get_number():
    print (n)

#for i in [12, 34, 5, 65]:
#    print (i)


