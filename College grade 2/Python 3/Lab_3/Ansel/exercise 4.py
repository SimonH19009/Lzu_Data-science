print("Below you will find information about the student you are registering.\n"
      "Enter a space in number if it ends.\n")
i=1
numberlist=[]
gradelist=[]
try:
    while True:
        num=input("Please enter the number of the student "+str(i)+":")
        if num:
            num=str(num)
            int(num)
            g1=float(input("Please enter the grade1:"))
            g2=float(input("Please enter the grade2:"))
            a=[i,g1,g2]
            i = i + 1
            gradelist.append(a)
            numberlist.append(num)
        else:break
except:
    print("Please enter a number!")

adic=dict(zip(numberlist,gradelist))
for key,value in adic.items():
    print("\nStudent " + str(value[0]) + " number:" + str(key))
    print("Student " + str(key) + " grade 1:" + str(value[1]))
    print("Student " + str(key) + " grade 2:" + str(value[2]))
print("\n{0:<7} {1:^7} {2:^7} {3:^6}".format("Number","Grade1","Grade2","Avg"))
for key,value in adic.items():
    avg=(value[1]+value[2])/2
    print("{0:<7} {1:^7} {2:^7} {3:^6}".format(key,value[1],value[2],avg))
