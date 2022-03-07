def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

s=input("Please enter a sentence:")
s=s.split()
num=len(s)
res=find_longest_word(s)

if num == 1:
    print(f"The sentence has 1 word and the longest word is {res}.")
else:
    print(f"The sentence has {num} words and the longest word is {res}.")