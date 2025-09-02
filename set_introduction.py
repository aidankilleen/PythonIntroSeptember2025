# set_introduction.py

fruit = {'apple', 'banana', 'apple', 'banana', 'strawberry'}
vegetables = {'carrot', 'lettuce', 'carrot', 'strawberry'}

print (fruit)
print (vegetables)

print (fruit | vegetables) # union operator
print (fruit & vegetables) # intersection
print (fruit - vegetables) # difference
print (vegetables - fruit) # difference

numbers = [1, 2, 3, 12,3, 2, 4, 5, 6, 2, 3, 2, 3, 2, 3, 10]

unique_numbers = set(numbers)
print (numbers)
print (unique_numbers)

