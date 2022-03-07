s = input("Please enter a sentence:")
list = s.split()
num = len(list)
longest_word = max(list,key=len)
if num == 1:
    print("The sentence has 1 word and the longest word is {longest_word}.")
else:
    print(f"The sentence has {num} words and the longest word is {longest_word}.")

# It just can return the first longest word. To do