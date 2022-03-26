str = input("Please enter a string:")
counter = {}
for i in str:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)