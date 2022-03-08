import sys

numbers = []
sum = 0
lowest = None
highest = None
count = 0
try:
    while True:
        line = input("Enter a number or Enter to finish:")
        if line:
            line = int(line)
            numbers.append(line)
        else:
            break
except ValueError:
        print("illegal input")
        sys.exit(0)
else:
    count = len(numbers)
    lowest = min(numbers)
    highest = max(numbers)
    for i in numbers:
        sum += i
        mean = sum / count
print("numbers:",numbers)
print("count = ",count,"sum = ",sum,"lowest = ",lowest,"highest = ",highest,"mean = ",mean)
