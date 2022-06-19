
import sys


print ("#####################################################################")
print ("############# A nice day starts with a cup of coffee! ###############")
print ("#####################################################################")
print ("1. Cappuccino [Water: 50ml; Milk: 50ml; Coffee: 50ml]: 12￥")
print ("2. Latte [Water: 80ml; Milk: 20ml; Coffee: 50ml]: 10￥")
print ("3. Mocha [Water: 50ml; Milk: 50ml; Coffee: 40ml; Mocha: 10ml]: 15￥")
print ("4. Cafe Americano [Water: 100ml; Milk: 0ml; Coffee: 50ml]: 10￥")
print ("5. Espresso [Water: 70ml; Milk: 0ml; Coffee: 80ml]: 14￥")
print ("   Quit [Q/q]")
print ("#####################################################################")

legalinput = ["1","2","3","4","5","Q","q"]
li = ["y","n"]
material = {'Water': 10000, 'Milk': 10000, 'Coffee': 10000, 'Mocha': 10000}

coffee_list = [[50, 50, 50, 0], [80, 20, 0, 0], [50, 50, 40, 10], [100, 0, 50, 0], [70, 0, 80, 0]]
coupon_num = ["12345", "6789"]

price = [0, 12, 10, 15, 10, 14]


soldaccount = {'cappuccino': 0, 'latte': 0, 'mocha': 0, 'cafe americano': 0, 'espresso': 0}
total = int(0)



def main():
    global item
    while True:
        item = input("please select your item:")
        if item in legalinput:
            if item == "q" or item == "Q":
                sys.exit()
            else:
                item = int(item)
                global list_price
                list_price = price[item]
                for value in material.values():
                    for v in coffee_list[item-1]:
                        if value < v:
                            print ("there are not enough.")
                            break
                        else:
                            continue        
                cif = input ("your item is available, please enter'c' to continue:")
                if cif == "c":   
                    coupon ()
                else:
                    print ("please input correctly.")
            break                           
        else:
            print ("please input correctly.")

def coupon ():
    global price
    while True:
        ans = input("a coupon is available? [y/n]:")
        if ans in li:
            if ans == "y":
                num = input("please enter your coupon No.:")
                if num in coupon_num:
                    price = list_price * 0.8
                    print (f"you have a coupon with 80% discount, your item price is:{price}.")
                    cash()
                else:
                    print ("your coupon is error.")
            else:
                price = list_price * 1
                cash()
            break
        else:
            print ("please input correctly.")
        
def cash():
    try:
        twe = int(input("please enter your cash, how many 20￥count? :"))
        ten = int(input("how many 10￥count? :"))
        five = int(input("how many 5￥count? :"))
        one = int(input("how many 1￥count? :"))
    except ValueError:
        print ("please input correctly.")
    else:
        amount = int(twe)*20 + int(ten)*10 + int(five)*5 + int(one)*1
        print(f"your total amount is:{amount}")
        if amount >= price:
            print(f"you change is:{amount-price},please receipt it.")
            print("your coffee is making:")
            print("……………………………….")
            print("## coffee preparing finished!")
            print("……………………………….")
            print("## coffee making finished!")
            print("……………………………….")
            print("## coffee packaging finished!")
            print("Please take you coffee carefully!")       
        else:
            while True:
                con = input("you have not enough money amount for buying, please continue to enter your cash [c] or quit with [q]:")
                if con == "c":
                    cash()
                elif con == "q":
                    sys.exit()
                else:
                    print ("please input correctly.")
    


def counter():
    
    a = list(soldaccount.keys())[item]
    soldaccount[a] = soldaccount[a] + 1
    total = total + price
    for j,k in soldaccount.items:
        print(soldaccount)
    print(f"### Total profile: {total}")


main()


        

        
# def process():
# print("")        
# your coffee is making:
# ……………………………….
# ## coffee preparing finished!
# ……………………………….
# ## coffee making finished!
# ……………………………….
# ## coffee packaging finished!
# Please take you coffee carefully!



# The items sold on this machine are:
# Cappuccino: 0
# Latte: 0
# Mocha: 1 
# Cafe Americano: 0 
# Espresso: 0
### Total profile: 12.0