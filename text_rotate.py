# text_rotate.py


import time

# exercise
# convert this to a function
# function takes in the message
# function takes in "direction" 1 = left to right 2 = right to left
# function takes in "speed" - this is the delay small = fast big = slow

# make this a command line utility where I can pass in the message and the other parameters
# from the command line

# 10.50

# hit "yes" when finished


def text_rotate(message, direction=1, speed=0.25, iterations=10000):
    for i in range(iterations):
        if direction == 1:
            # left to right
            message = message[-1]+ message[:-1]
        else:
            # right to left
            message = message[1:] + message[0]

        print (message, end="\r")
        time.sleep(speed)

if __name__ == "__main__":
    message = "This is a message"

    text_rotate(message, 2, 0.1)

