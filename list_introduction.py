#   list_introduction.py
numbers = [3, 2, 5, 4, 1, 6, 9]
print (numbers[1]) # list index start at 0
print (numbers[0]) # first item in the list
#print (numbers[99]) # can't access an item outside the list
print (len(numbers)) # length of the list
index = 0

# non python way of iterating a list
while index < len(numbers):
    print (numbers[index])
    index += 1

# iterating with an index - not really the python way of doing things
for n in range(len(numbers)):
    print (numbers[n])

# pythonic way of iterating a list  
for item in numbers:
    print (item)

print ("*"*25)
# negative index - take from the end of the list
print (numbers[-1])

# slicing
print (numbers)

print (numbers[1:4])    # start at 1(inclusive) go to 4(exclusive)

print (numbers[1:]) # leave out the second number and it goes to the end
print (numbers[:4]) # leave out the first number and it goes from the beginning

list_copy = numbers[:]  # leave out both numbers and it makes a copy of the list
print (list_copy)

# lists are mutable
numbers[0] = 999
print (numbers)


#gotcha! - do not use the variable name "list"
#python doesn't show an error if you reassign a built in function name
#list()
#list = [1,2,3,4] # a normal programming language would prevent you from doing this - python doesn't
#print = 27
#print()

numbers = list(range(10))

print (numbers)

new_list = numbers[1:9:2] # start, end, step
print (new_list)

new_list = numbers[::3]
print (new_list)

another_list = list(range(1, 20, 3))
print (another_list)

# all of these work on strings!!!
test_string = "this is a test string"
print (test_string)
print (test_string[0]) # first letter
print (test_string[-1]) # last letter

print (test_string[5:8])

print (test_string[:5])
print (test_string[5:]) 

print (test_string[::2])


domain = "amazon.com"

print (domain[-3:]) # extract last 3 letters from string using negative index
print(domain[::-1]) # reverse the string


# strings are immutable!
# domain[0] = "A"

domain = "A" + domain[1:]
print (domain)









