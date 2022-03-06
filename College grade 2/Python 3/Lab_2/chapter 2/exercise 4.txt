try:
    a=input("Please enter a sentence:")
    a=a.split()
    num=len(a)
    res = max(a, key=len, default='')
    print("The sentence has "+str(num)+" sentences and the longest word is "+str(res)+".")
except:
    print("no correct")

