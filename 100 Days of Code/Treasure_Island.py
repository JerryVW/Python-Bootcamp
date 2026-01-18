print(
    r'''
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
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = (
    input("You're at a cross road. Where do you want to go?" "Type 'left' or 'right'.")
).lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    to_the_island = input(
        "Type 'wait' tp wait for the boat. Type 'swim' to swim across."
    ).lower()
    if to_the_island == "wait":
        print("You arrive at the island unharmed. There is a house with three doors")
        choice_of_door = input(
            "One red, one yellow, and on blue. Which door do you choose?"
        ).lower()
        if choice_of_door == "red":
            print("You were burned to death by fire!")
            print("GAME OVER!")
        elif choice_of_door == "yellow":
            print("Bingo!! You have found the treasure!!")
            print("YOU WIN!!")
        elif choice_of_door == "blue":
            print("You were eaten by the great beast!")
            print("GAME OVER!")
        else:
            print("There is no other way!!")
    elif to_the_island == "swim":
        print("You were swallowed by the Lochness Monster!!")
        print("GAME OVER!")
    else:
        print("There is no way in that manner to cross the lake.")

elif direction == "right":
    print("Oh No! You fell in a hole!")
    print("GAME OVER!")
else:
    print("That direction is not an option!")
# Day Three
