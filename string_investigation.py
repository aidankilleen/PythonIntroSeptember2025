# string_investigation.py


message = "this is a message"

# iterate a string -> returns one letter at a time
for c in message:
    print (c)


pieces = message.split()
print (pieces)

csvvalues = "Aidan,Cork,0872034567,Technical Trainer"

items = csvvalues.split(",")
print (items)


value = input("Enter a number:")

if value.isnumeric():
    v = int(value)
else:
    print ("invalid number")
    v = 0

print (f"The value is {v}")

message = "this is a message"

words = message.split()

words = [word.capitalize() for word in words]

print (words)

print (",".join(words))











