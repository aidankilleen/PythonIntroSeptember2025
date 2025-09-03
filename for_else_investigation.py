# for_else_investigation.py
numbers = [1, 5, 4, 2, 99, 6, 8, 9, 3]

for number in numbers:
    if number == 6:
        # don't print out 6
        print ("Skipping 6")
        continue # go to the next iteration of the loop
    elif number == 99:
        print ("Error - can't continue")
        break   # break terminates the loop
    else:
        print (number)
else:
    #else clause means that the loop ran without a break
    print ("else clause activated")

print ("finished")

