# string_introduction.py


name = "Aidan"

print ("Welcome " + name)

x = 10
y = 20
answer = x + y

# you can't concate a number to a string - str() function converts anything to a string
print ("The answer is " + str(answer))

# 10 + 20 = 30
print (str(x) + " + " + str(y) + " = " + str(answer))

# seems overly complex

# f strings allow me to substitue in variables into my string
# I use these almost exclusively
print (f"the answer is {answer}")

print (f"{x} + {y} = {answer}")

# nb: you can put expressions into your f strings if you like
print (f"{x} + {y} = {x + y}")

number = 49

print (f"{number} is {"big" if number > 50 else "small"}")

if number > 50:
    print (f"{number} is big")
else:
    print (f"{number} is small")


name = "aidan killeen"


print (name.capitalize())
print (name.title())

print (name.upper())

# strings are objects
# objects have values 
# and functions (methods)


values = [2, 5, 10, 24, 18, 5, 1]

for v in values:
    print (f"{v}\t" + "*" * v)