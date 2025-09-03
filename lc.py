# lc.py
import sys

print ("line counter")
try:
    filename = sys.argv[1]

    with open(filename, "r") as f:

        lines = f.readlines()
        print (f"{filename} has {len(lines)} lines")

except:
    print ("""lc.py 
Line Counter utility
Usage:
python lc.py FILE

""")



