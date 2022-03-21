string=input("Please enter a string:")
counter = {}
for i in string:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)
