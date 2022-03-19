string=input("Please enter a string:")
counter = set()
for i in string:
    a=string.count(i)
    tuple=(i,a)
    counter.add(tuple)
print(counter)

