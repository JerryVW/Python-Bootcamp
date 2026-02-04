import random

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randint(1, 100)
# print(random_number)
remaining_guesses = 0
not_right_number = True


if difficulty == "easy":
    remaining_guesses = 10
else:
    remaining_guesses = 5


def less_than(guess):
    if guess < random_number:
        global remaining_guesses
        print("Too low!")
        print("Guess again!")
        remaining_guesses -= 1
        print(f"You have {remaining_guesses} chances left to guess the number.")


def greater_than(guess):
    if guess > random_number:
        global remaining_guesses
        print("Too high!")
        print("Guess again!")
        remaining_guesses -= 1
        print(f"You have {remaining_guesses} chances left to guess the number.")


def equal_to(guess):
    if guess == random_number:
        global not_right_number
        print("You guessed the number!")
        not_right_number = False


print(f"You have {remaining_guesses} chances left to guess the number.")

while not_right_number:
    guess = int(input("Make a guess: "))
    equal_to(guess)
    less_than(guess)
    greater_than(guess)
