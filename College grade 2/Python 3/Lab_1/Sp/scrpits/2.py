from html.entities import name2codepoint


num1 = input("Please enter the first number:")
num2 = input("Please enter the second number:")
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Please enter the legal text.")
else:
    if num1%num2 == 0:
        print (num1,"is a multiple of",num2)
    else:
        print(num1,"is not a multiple of",num2)