import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

random_choice = random.randint(0, 2)
computer_choice = [rock, paper, scissors]
player_choice = [rock, paper, scissors]
player_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
)
# print(f"{player_choice[player_input]} vs {computer_choice[random_choice]}")
if player_input >= 0 and player_input <= 2:
    if (
        player_choice[player_input] == rock
        and computer_choice[random_choice] == scissors
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Rock beats scissors! You win!")
    elif (
        player_choice[player_input] == scissors
        and computer_choice[random_choice] == paper
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Scissors beats paper! You win!")
    elif (
        player_choice[player_input] == paper and computer_choice[random_choice] == rock
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Paper beats rock! You win!")

    elif (
        computer_choice[random_choice] == rock
        and player_choice[player_input] == scissors
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Rock beats scissors! You lose!")
    elif (
        computer_choice[random_choice] == scissors
        and player_choice[player_input] == paper
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Scissors beats paper! You lose!")
    elif (
        computer_choice[random_choice] == paper and player_choice[player_input] == rock
    ):
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("Paper beats rock! You lose!")

    elif player_choice[player_input] == computer_choice[random_choice]:
        print("Player chose:")
        print(player_choice[player_input])
        print("computer chose:")
        print(computer_choice[random_choice])
        print("It's a Draw!")
else:
    print("Not a valid input!")
# Day Four
