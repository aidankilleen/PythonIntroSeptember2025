# loop_enumerate_investigation.py
for i in range(10):
    print (i)

names = ["Alice", "Bob", "Carol", "Dan", "Eve"]

for name in names:
    print (name)

# this is not the python way!!!
for i in range(len(names)):
    print (f"{i+1}\t{names[i]}")

# this is the python way to get an index!!
for index, name in enumerate(names):
    print (f"{index+1}\t{name}")







