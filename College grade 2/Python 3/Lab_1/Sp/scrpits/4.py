r=input("Please enter the radius of the circle:")
pi=3.1416
try:
    r = float(r)
except ValueError:
    print("You have not inserted a valid number!")
else:
    p=2*pi*float(r)
    a=pi*float(r)**2
    print("Perimeter:",p)
    print("Area:",a)