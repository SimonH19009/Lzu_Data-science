import random
articles=["the","a","another"]
subjects=["cat","dog","man","man"]
verb=["sang","ran","jump"]
adverbs=["loudly","quietly","well","badly",""]
all=[articles,subjects,verb,adverbs]
for i in range(5):
    list=[]
    for i in all:
        j=random.randint(0,len(i)-1)
        list.append(i[j])
    print(list[0],list[1],list[2],list[3])
