from collections import Counter

str = input("Please enter a string:")
a = list(Counter(str).items())
print (a)