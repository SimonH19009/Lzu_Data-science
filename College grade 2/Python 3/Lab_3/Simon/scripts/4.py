print("Please enter the student you are registering.\n"
      "Enter a space in number if it ends.\n")
i = 1
numberlist = []
gradelist = []
try:
    while True:
        num = input(f"Student {i} number:")
        if num:
            num = str(num)
            int (num)
            g1 = float(input(f"Student {num} grade1:"))
            g2 = float(input(f"Student {num} grade2:"))
            a = [i,g1,g2]
            i = i + 1
            gradelist.append(a)
            numberlist.append(num)
            print ("")
        else:
            break
except:
    print ("Please enter a number!")
else:
adic = dict(zip(numberlist,gradelist))
for key,value in adic.items():
    print (f"\nStudent {value[0]}  number: {key}")
    print (f"Student {key}  grade 1: {value[1]}")
    print (f"Student {key} grade 2: {value[2]}")
print ("\n{0:<7} {1:^7} {2:^7} {3:^6}".format("Number","Grade1","Grade2","Avg"))
for key,value in adic.items():
    avg = (value[1] + value[2]) / 2
    print ("{0:<7} {1:^7} {2:^7} {3:^6}".format(key,value[1],value[2],avg))