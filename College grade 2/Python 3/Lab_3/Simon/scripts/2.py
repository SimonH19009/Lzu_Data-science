str = input("Please enter a string:")
counter = set()
for i in str:
    a = str.count(i)
    tuple = (i,a)
    counter.add(tuple)
print (counter)