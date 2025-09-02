# tuple_introduction.py

t = (5, 4, 2, 7, 8, 1)

print (t)
print (t[0]) # first item
print (len(t))

#print (t[99])

print (t[-1]) 
print (t[2:5])
print (t[:5])
print (t[5:])
print (t[::2])

print (t[::-1])

# tuple is an immutable list - you can't change its contents!
# t[0] = 999


for item in t:
    print (item)


tuple_copy = t[:]

print (tuple_copy)

print (t)
t = t + (5, 2, 5)

print (t)
print(t.count(5))


# uses for tuples

# returning multiple values from a function
def process_list(numbers):
    total = sum(numbers)
    count = len(numbers)
    return (total, count)


number = [2, 4, 3, 1, 5, 6, 10]
answer = process_list(number)   

# answer[0] = 999

print (f"The total is {answer[0]}")
print (f"The count is {answer[1]}")


# swap two variables

a = 10
b = 20

print (f"a={a} b={b}")
t = b
b = a
a = t

print (f"a={a} b={b}")


# in python we can use a tuple to swap two variables

a = 10
b = 20
print (f"a={a} b={b}")

(a, b) = (b, a)

print (f"a={a} b={b}")

# make multiple assignments

# instead of
#a = 10
#b = 20
#c = 30

# do this instead
(a, b, c) = (10, 20, 30)


# you can sometimes leave out the round brackets

a, b, c, = 10, 20, 30

# I prefer to leave in the brackets because it clearer whats going on


t = (1, 2, 3, 4, 5, 6, 7)

(a, b, *others) = t

print (f"a={a} b={b}")
print (others)

print (t)

