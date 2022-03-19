list=[5, 4, 1, 8, 5, 2]
list.sort()
a=len(list)
if a%2==0:
   number=list[int(a/2-1)]+list[int(a/2)]
   median=number/2
else:
    number=int((a+1)/2-1)
    median=list[number]
print("the median= ",median)