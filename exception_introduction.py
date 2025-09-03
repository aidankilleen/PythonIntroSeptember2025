# exception_introduction.py
import random

numbers = [1, 2, 3]
x = 10
y = 0
s = "ninety nine"

r = random.randint(1, 4)
try:
    if r == 1:
        answer = int(s)
    elif r == 2:
        answer = numbers[3]
    elif r == 3:
        answer = x / y
    else:
        answer = 42
except IndexError:
    print ("can't access index 3")
    answer = numbers[0]
except ZeroDivisionError:
    print ("can't divide by zero")
    answer = 0
except:
    # catch all other potential problems 
    print ("something went wrong") 
    answer = 99
else:
    print ("no error occurred")
finally:
    # gets called no matter what - 
    print (f"The answer is {answer}")
print ("Finished")








#

#








# c++

# glass is half full style
# c++, Java, C#, added to python

""" try:
    do_something()
    do_something_else()

NetworkException:
    print ("network error")
FileException:
    print ("file error")
UserException:
    print ("user error")
Exception:
    print ("some other error")

 """


# glass is half empty style of coding
# c - programmer
""" r = do_something()
if r == 0:
    print ("it worked")
elif r == -1:
    print ("network error")
elif r == -2: 
    print ("file error")
elif r == -3:
    print ("user error")
else:
    print ("some other error")

r = do_something_else()
if r == 0:
    print ("it worked")
elif r == -1:
    print ("network error")
elif r == -2: 
    print ("file error")
elif r == -3:
    print ("user error")
else:
    print ("some other error")
 """













