from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

coins = 0
change = round(change * 100)

coins += change // 25
change -= (change // 25) * 25
coins += change // 10
change -= (change // 10) * 10
coins += change // 5
change -= (change // 5) * 5
coins += change

print(int(coins))
