from cs50 import get_int

while True:
    card = get_int("Number: ")
    if card > 0:
        break

card_save = card
yes_multiply = 0
no_multiply = 0

while card > 0:
    no_multiply += card % 10
    card //= 10
    multiply_num = (card % 10) * 2
    if multiply_num >= 10:
        yes_multiply += (multiply_num % 10)
        yes_multiply += 1
    else:
        yes_multiply += multiply_num
    card //= 10

legit = False

if ((yes_multiply + no_multiply) % 10 == 0):
    legit = True

if (card_save >= 100000000000000 and card_save <= 999999999999999) and ((card_save // 10000000000000)==34 or (card_save // 10000000000000)==37) and legit:
        print("AMEX")
elif ((card_save >= 1000000000000000 and card_save <= 9999999999999999) and
    ((card_save // 100000000000000)==51 or (card_save // 100000000000000)==52 or
    (card_save // 100000000000000)==53 or (card_save // 100000000000000)==54 or
    (card_save // 100000000000000)==55) and
    legit):
        print("MASTERCARD")
elif ((((card_save >= 1000000000000 and card_save <= 9999999999999) and
        ((card_save // 1000000000000) == 4)) or
        ((card_save >= 1000000000000000 and card_save <= 9999999999999999) and
        ((card_save // 1000000000000000) == 4))) and
        legit):
        print("VISA")
else:
        print("INVALID")
