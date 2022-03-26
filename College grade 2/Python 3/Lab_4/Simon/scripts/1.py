def div(n1,n2):
    d = n1 // n2
    r = n1 - n2 * d
    print(r)
while True:
    try:
        num1 = float(input("Please enter the first number:"))
        num2 = float(input("Please enter the second number:"))
    except ValueError:
        print("Please enter the number correctly.")
    else:
        div(num1,num2)
        break