def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
try:
    a=input("Please enter a sentence:")
    a=a.split()
    num=len(a)
    res=find_longest_word(a)
    print("The sentence has "+str(num)+" sentences and the longest word is "+str(res)+".")
except:
    print("no correct")
