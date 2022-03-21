def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
try:
    a=input("Please enter a sentence:")
    a=a.split()
    a[len(a)-1]=(a[len(a)-1].strip( '.' ))
    num=len(a)
    res=find_longest_word(a)
    if num != 1:
        print("The sentence has " + str(num) + " words and the longest word is " + str(res) + ".")
    else:
        print("The sentence has " + str(num) + " word and the longest word is " + str(res) + ".")
except:
    print("no correct")
