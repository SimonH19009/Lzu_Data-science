import random
articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl","They"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw","heard", "felt", "slept", "cried","laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "badly","rudely", "politely"]
i = 0
while i < 5:
    line = ""
    line += random.choice(articles) + " "
    line += random.choice(subjects) + " "
    line += random.choice(verbs) + " "
    r = random.randint(1,2)
    if r == 2:
        line += random.choice(adverbs) + " "
    print(line)
    i += 1