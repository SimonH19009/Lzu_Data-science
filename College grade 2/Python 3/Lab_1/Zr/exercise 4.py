r=input("Please enter the radius of the circle:")
try:
    pi=3.1416
    p=2*pi*float(r)
except ValueError:
    print("You have no inserted a valid number!")
else:
    a=pi*float(r)*float(r)
    print("Perimeter:"+str(p))
    print("Area:"+str(a))