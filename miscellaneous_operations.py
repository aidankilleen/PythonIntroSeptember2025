# miscellaneous_operations.py

x = 10
y = 2

# division always returns a float
answer = x / y
print (x, y)


print (answer)


# integer division

answer = x // y
print (answer)

x = 10
y = 3

print (f"{x} / {y} = {x/y}")
print (f"{x} // {y} = {x//y} r{x%y}")

# unary operators
x = 10
x = -x

print (x)

# increment
x = 10

x = x + 1
print (x)

x += 1
print (x)

#x++ # does not work

# power operator
answer = 2 ** 3
print (f"2**3 = {answer}")

# number bases
n = 10 # decimal

n = 0b10 # binary
print (n)

n = 0x10 # hexadecimal
print (n)

n = 0o10 # octal
print (n)

# use f strings to format

n = 0b10000000
print (n)

print (f"{n:08b}")

n = 0xffff
print (n)
print (f"{n:08x}")

# binary operators
n = 0b10000000

print (f"{n:08b}")

#n = n >> 1
n >>= 1

print (f"{n:08b}")

n = 64
print (n)
print (n>>1)


n = 0b1010001

print (f"{n:08b}")
print (f"{~n:08b}") # not 


a = 0b001001
b = 0b111011
answer = a & b

print (f"{a:08b}")
print (f"{b:08b}")

print (f"{answer:08b}")

print ("*"*25)

# some formatting examples
answer = 1

x = 123.45678
y = 4321.65432
print (f"{x:8.2f}")
print (f"{y:8.2f}")
print ("-" * 10)
print (f"{x+y:8.2f} ")

name = "Aidan"
print (f"{name:>20}")


# order of operations

a = 10
b = 20
c = 30

answer = a / b * c + b - a ** 3 # which order does this work in

# PEMDAS - Parenthesis (Brackets) Exponent Multiplication Division Addition Subtraction

answer = ((a / b) * c) + ((b - a) ** 3)

print ("*" * 25)




# id()
a = 10

print (id(a))

# strings are immutable
name = "Aidan"
print (name, id(name))
# changes to the variable instantiate a new value with a different id
name = "Aidan Killeen"
print (name, id(name))


# if you have 2 variables with the same value
# python might use the same area in memory(same id) as an optimisation
name = "Alice"
name2 = "Alice"

print (name, id(name))
print (name2, id(name2))


l1 = (1, 2, 3)
l2 = (1, 2, 3)
print (id(l1), l1)
print (id(l2), l2)

l1 = l1 + (4, )     # if you want to create a tuple with 1 item you need the ,

print (id(l1), l1)
print (id(l2), l2)
































































