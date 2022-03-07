import sys
import unicodedata

def print_unicode_table(word):
    titleList = ["decimal", "hex", "chr", "name"]
    print("{0[0]:7}{0[1]:^5}{0[2]:>3}{0[3]:^40}".format(titleList))
    print("-------  -----  ---  {0:-<40}".format(""))
    #Table header
    code = ord(" ")
    end = min(0xD800, sys.maxunicode)
    # Stop at surrogate pairs
    while code < end:
        c = chr(code)  #c=chracter
        name = unicodedata.name(c, "*** unknown ***")  #name=the name of c
        ok = True
        for word in words:
            #As long as there is a word that is not in the name then ok=false
            if word not in name.lower():
                ok = False
                break
        if ok:
            #if word not be found in this line,then turn to the next
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                code, name.title()))
        code += 1

words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        #if user need the help,print the usage
        print("usage: {0}  [string1 [string2 [... stringN]]]".format(sys.argv[0]))
        words = None
    else:
        #Split vocabulary and merge list
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(word)
