import random
import sys
articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl","They"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw","heard", "felt", "slept", "cried","laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "badly","rudely", "politely"]
i = 0
j = input("Please enter the number of lines of poetry:")
if j:
    try:
        j = int(j)
    except ValueError:
        print("Please enter the number.")
        sys.exit(0)
    else:
        if 1 <= j <= 10:
            j = j
        else:
            print("Number of lines must be 1-10 inclusive.")
            sys.exit(0)
else:
    j = int(5)
while i < j:
    line = ""
    line += random.choice(articles) + " "
    line += random.choice(subjects) + " "
    line += random.choice(verbs) + " "
    r = random.randint(1,2)
    if r == 2:
        line += random.choice(adverbs) + " "
    print(line)
    i += 1