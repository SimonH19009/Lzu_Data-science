s = input("Please enter the number of seconds:")
try:
    s = int(s)
    s0 = s
except ValueError:
    print("Please enter a number.")
else:
    if s >= 0:
        s = int(s)
        m,s = (divmod(s,60))
        h,m = (divmod(m,60))
        d,h = (divmod(h,24))
        print(f"{s0} seconds correspond to {d} day, {h} hours, {m} minutes and {s} seconds")
    else:
        print("Please enter a positive integer number.")