def div(a,b):
    i=0
    while True:
        if i*b >a:
            c=i-1
            break
        elif i*b==a:
            c=i
            break
        else:
            i=i+1
    return (a-c*b)

a=float(input("Please enter the first number:"))
b=float(input("Please enter the second number:"))
print(div(a,b))

