import random
articles=["the","a","another"]
subjects=["cat","dog","man","man"]
verb=["sang","ran","jump"]
adverbs=["loudly","quietly","well","badly",""]
all=[articles,subjects,verb,adverbs]
try:
    nu=int(input("Please enter the number of lines of poetry:"))
except ValueError:
    nu=5
for i in range(nu):
    list=[]
    for i in all:
        j=random.randint(0,len(i)-1)
        list.append(i[j])
    print(list[0],list[1],list[2],list[3])
