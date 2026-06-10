print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
answer1 = input("Type 'left' or 'right'\n").lower()
if answer1 == "left":
    print("You've come to a lake. The is an island in the middle of the lake.")
    answer2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across the lake.\n").lower()
    if answer2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        answer3 = input("One red, one yellow and one blue. Which color do you choose?\n").lower()
        if answer3 == "yellow":
            print("You found the treasure! You win!")
        elif answer3 == "blue":
            print("You enter a room full of hungry beasts. Game Over.")
        else:
            print("You enter a lava floor room and it's burned by the fire. Game Over.")
    else:
        print("You're attacked by a trout. Game Over.")
else:
    print("You've fell into a hole. Game Over.")




