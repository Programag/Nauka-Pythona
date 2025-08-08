import random

gameLength = 5

getChest = ["Yes", "No"]

chests = [["Green", 1000], ["Orange", 4000], ["Purple", 9000], ["Gold (legendary)", 16000]]

money = 0

def findApproximateValue(value):
    global money
    lowestValue = value[0][1] * 0.1
    highestValue = value[0][1] * 0.1
    choice = random.choice([0, 1])
    if choice == 0:
        recent_prize = value[0][1] - lowestValue
        money += recent_prize
    if choice == 1:
        recent_prize = value[0][1] + highestValue
        money += recent_prize
    print(f"{value[0][0]} chest is worth {recent_prize:.0f} coins.")
    print(f"Your balance is now equal to {money:.0f}.")

def findChest(treasure):
    global money
    picked_chest = random.choices(treasure, weights=[75, 20, 4, 1])
    print(f"You've found {picked_chest[0][0]} chest.")
    findApproximateValue(picked_chest)



print('''Welcome in my treasure looking game.
You have only 5 steps and your goal is to find as much coins as possible.''')

while gameLength > 0:
    answer = input("Do you want to go forward? ")
    if answer.lower() == "yes":
        did_find_chest = random.choices(getChest, weights=[60, 40])
        if did_find_chest[0] == "Yes":
            findChest(chests)
        else:
            print("You didn't find chest on your move.")
    elif answer.lower() == "no":
        break
    gameLength = gameLength - 1
    if gameLength == 0:
        print("No more moves left!")
    print("\n")

print(f"Congratulations, you've found {money:.0f} coins.")