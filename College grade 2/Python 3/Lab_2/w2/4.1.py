s = input("Please enter a sentence:")
s = s.split()
s[len(s)-1]=(s[len(s)-1].strip( '.' ))
num = len(s)
longest_word = max(s,key=len)
if num == 1:
    print(f"The sentence has 1 word and the longest word is {longest_word}.")
else:
    print(f"The sentence has {num} words and the longest word is {longest_word}.")

# It just can return the first longest word. To do