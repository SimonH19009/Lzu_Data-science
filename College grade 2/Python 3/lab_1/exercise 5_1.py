import sys
Zero=['*****','*   *','*   *','*   *','*   *','*   *','*****']#0
One=['  *  ',' **  ','* *  ','  *  ','  *  ','  *  ','*****']#1
Two=['*****','    *','    *','*****','*    ','*    ','*****']#2
Three=['*****','    *','    *','*****','    *','    *','*****']#3
Four=['  *  ',' **  ','* *  ','*****','  *  ','  *  ','  *  ']#4
Five=['*****','*    ','*    ','*****','    *','    *','*****']#5
Six=['*****','*    ','*    ','*****','*   *','*   *','*****']#6
Seven=['*****','    *','    *','   * ','  *  ',' *   ','*    ']#7
Eight=['*****','*   *','*   *','*****','*   *','*   *','*****']#8
Nine=['*****','*   *','*   *','*****','    *','    *','*****']#9
Digits=[Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

try:
    digits ="123"   #Locate the desired string
    row = 0                #Initialize the number of rows
    while row < 7:
        column = 0         #Initialize the number of number
        line = " "
        while column < len(digits):          #When the printed characters are less than the total number of characters
            number = int(digits[column])     #number=The ordinal number of the character being printed
            length = Digits[number]
            add = length[row]                #Locates a definitive row of a digital drawing
            change = 0                       #Initializes the retrieval sequence number
            changes = ""                     #Initializes the replacement character
            while change < len(add):
                if add[change] == "*":       #Retrieves the asterisk
                    changes += str(number)   #If so, stitch the numbers together
                else:
                    changes += " "           #If not, stitch the spaces
                change += 1                  #Add one to the serial number and enter the loop until the detection is complete
            add = changes                    #Replace the characters
            line += add + " "                #A separator between numbers
            column += 1                      #Replace the characters
        print(line)
        row += 1                             #print the next line
except ValueError as err:
        print(err)
except IndexError:
        print("Your input is illegal")
