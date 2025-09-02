# building_blocks.py
# basic building blocks for python
# Date: 2/9/2025
# By: Aidan

# BB #1 - Comments


print ("hello") 

"""
this
is 
a multi-line comment
"""


# Building Block #2 - Variables
name = "Aidan"
num = 25
PI = 3.14
x = 10
y = 20

name = "Aidan Killeen"
firstName = "Aidan" # lower camel case - do not use this in python
first_name = "Aidan" # snake case - use this in python

# python can handle really long numbers 
n = 12387623458762345987623948756239847562983476582763459826982436598273
print(n)
n = "ninety nine"

# python is weakly typed - no error if you change the type of a variable
print (n)


# Building Block #3 - expressions

answer = 10 * 20
answer = x + y 
print (n * 10)

# you can multiply a string
print ("*" * 25)


# Building Block #4 - conditions

age = int(input("What is your age?"))

if age < 18:
    print ("You are a minor")
elif age <= 65:
    print ("You are an adult")
else:
    print("you are retired")

# single line conditions
message = "you are " + "a minor" if age < 18 else "an adult" if age <= 65 else "retired"

# Building Block #5 - Loops

count = 1

while count <= 10:
    print (count)
    count = count + 1


# for loop - iterating items in a list
print("*" * 25)
lst = [1, 2, 3, 4]
for i in lst:
    print (i)

print("*" * 25)
for i in range(10):
    print (i)


# Building Block #6 - Functions
print()
int(3.23456)
range(10)


def greet(name):
    print ("Hello, " + name)


greet("Aidan")
greet("Alice")


# building block #7 - lists
# python has a very rich feature set for working with lists and collections of items


# building block #8 - objects
# python is an object oriented programming language





























