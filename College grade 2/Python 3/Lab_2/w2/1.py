num = input ("Please enter a number:")
try:
    num = int(num)
except ValueError:
        print("Please enter a two-digit positive integer number.")
else:
    if 10 <= num <= 99:
        x = (num / 10)
        x = int(x)
        y = num - 10 * x
        print(x)
        print(y)
    else:
        print("Please enter a two-digit positive integer number.")
