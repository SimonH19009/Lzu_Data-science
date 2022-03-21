string=input("Please enter a string:")
re=[]
counter = []
for i in string:
    if i not in re:
       a=string.count(i)
       tuple=(i,a)
       counter.append(tuple)
       re.append(i)
print(counter)

#Another method
'''from collections import Counter
string=input("Please enter a string:")
dic=list(Counter(string).items())
print(dic)'''
