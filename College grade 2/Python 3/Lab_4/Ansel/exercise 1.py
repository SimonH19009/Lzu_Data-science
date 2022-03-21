def div(a,b):
    i=0
    while True:
        if i*b >a:
            return i-1
            break
        elif i*b==a:
            return i
        else:
            i=i+1

a=float(input("Please enter the first number:"))
b=float(input("Please enter the second number:"))
print(div(a,b))

