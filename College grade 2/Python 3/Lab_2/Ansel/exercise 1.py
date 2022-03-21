try:
    a=int(input("Please enter a number:"))
    if 9<a<100:
        a = str(a)
        print(a[0])
        print(a[1])
    else:
        print("no correct")
except:
    print("no correct")
