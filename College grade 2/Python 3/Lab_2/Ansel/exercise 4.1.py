try:
    a=input("Please enter a sentence:")
    a=a.split()
    a[len(a)-1]=(a[len(a)-1].strip( '.' ))
    num=len(a)
    res = max(a, key=len, default='')
    if num!=1:
        print("The sentence has "+str(num)+" words and the longest word is "+str(res)+".")
    else:
        print("The sentence has " + str(num) + " word and the longest word is " + str(res) + ".")
except:
    print("no correct")




