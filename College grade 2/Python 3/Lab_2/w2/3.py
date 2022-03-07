w = input("Please enter the string:")
if w == w[::-1] :
    print(f"{w} is a palindrome.")
else:
    print(f"{w} is not a palindrome.")