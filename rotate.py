# rotate.py

import sys

from text_rotate import text_rotate
print (sys.argv)


message = sys.argv[1]
direction = sys.argv[2]
speed = sys.argv[3]


text_rotate(message, int(direction), float(speed))


#TBD
# handle missing parameters properly
# add docstring comments
# add "usage" message to the command line utility






