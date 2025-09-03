# while_else_investigation.py

numbers = [1, 4, 2, 3, 6, 77, 5, 9]
index = 0

while index < len(numbers):

    if numbers[index] == 7:
        print ("Found the number 7")
        break

    index = index + 1
else:
    # else activated if the loop runs without encountering a break
    print ("7 not found")

