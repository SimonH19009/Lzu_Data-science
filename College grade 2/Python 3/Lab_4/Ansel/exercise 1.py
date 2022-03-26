def div(a,b):
    i=0
    while True:
        if (a-(i*b))>0:
            i=i+1
        if (a-(i*b))==0:
            return 0
        if (a-(i*b))<0:
            return (a-(i-1)*b)
    return (a-c*b)

a=float(input("Please enter the first number:"))
b=float(input("Please enter the second number:"))
print(div(a,b))


