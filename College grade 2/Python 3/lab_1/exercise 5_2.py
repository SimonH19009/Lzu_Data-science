list=[]
try:
    while True:
        a=input("enter a number or Enter to finish:")
        if a:
            a=int(a)
            list.append(a)
        else:
            break
    print("number="+str(list))
    count = len(list)
    sum=sum(list)
    lowest=min(list)
    highest=max(list)
    mean=sum/count
    print("count="+str(count),"sum="+str(sum),"lowest="+str(lowest),"highest="+str(highest),"mean="+str(mean))
except ValueError:
    print("Your input is illegal")
