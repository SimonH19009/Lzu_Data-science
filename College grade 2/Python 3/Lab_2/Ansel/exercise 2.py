try:
    a=int(input("Please enter the number of seconds:"))
    if a>=0:
        day=divmod(a,86400)[0]
        hours=divmod(a,86400)[1]//3600
        minutes=(a-86400*day-3600*hours)//60
        seconds=(a-86400*day-3600*hours-60*minutes)
        print(a,"seconds correspond to",day,"day,",hours,"hours,",minutes,"minutes,and",seconds,"seconds")
    else:
        print("no correct")
except:
    print("no correct")

