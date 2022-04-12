import sys

def printf(w,l,c):
    for i in range(l):
        if i != 0 and i != (l-1):
            print (w + " " * (c - 2) + w)
        else:
            print (w * c)
try:
    char = input("Please enter a character ('q' to quit):")
    if char == "q":
        print (" character 'q' is not allowed to be entered.How am I supposed to know?Please ask to the Prof.Guo.")
        sys.exit()
    else:
        lines = int(input("Please enter the number of lines:"))
        columns = int(input("Please enter the number of columns:"))
except ValueError:
    print ("Please enter them correctly.")
else:
    printf(char,lines,columns)