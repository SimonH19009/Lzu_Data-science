import string
import sys
import collections

words=collections.defaultdict(int)
strip=string.whitespace+string.punctuation+string.digits+"\""

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word=word.strip(strip)
            if len(word)>2:
                words[word]=words[word]+1

def getValue(item):
    return item[1]

for word,number in sorted(words.items(),key=getValue):
    print("'{0}' occurs {1} times".format(word, number))

#the other method
'''words=dict(sorted(words.items(),key = lambda x:x[1],reverse=False))

for word in words:
    print("'{0}' occurs {1} times".format(word,words[word]))'''
