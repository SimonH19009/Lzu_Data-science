def drec(a,b,c):
    print(a*b)
    i=1
    while True:
        i = i + 1
        if i>(c-1):
            break
        else:print(a+" "*(b-2)+a)
    if c!=1:
        print(a*b)
try:
    a=input("Please enter a character:")
    c=input("Please enter the number of lines:")
    b=input("Please enter the number of columns:")
    drec(a,int(b),int(c))
except:
    print("Please enter correctly!!")
