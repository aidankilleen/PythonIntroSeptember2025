# fileio_introduction.py

#f = open("testfile.txt", "r")
#lines = f.readlines()
#print (lines)
#f.close()


with open("testfile.txt", "r") as f:

    lines = f.readlines()
    print (lines)


# note : no need to close the file
# with automatically tidies up f


# writing

with open("newfile.txt", "a") as f:

    # f.write("This is a test\n")
    print("This is a test", file=f)





with open("testfile.txt", "r") as f:

    # instead of calling readlines
    # we should iterate, particularly if we have a large file
    print (f)
    for line in f:
        print (line.strip())



print ("finished")

