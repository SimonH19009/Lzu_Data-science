number1=input("Please enter the first number:")
number2=input("Please enter the second number:")
try:
    number1=int(number1)
    number2=int(number2)
except ValueError:
    print("The text you entered is illegal!!")
else:
    if number1%number2==0:
        print(str(number1)+" is a multiple of "+str(number2))
    else:
        print(str(number1)+"is not a multiple of"+str(number2))