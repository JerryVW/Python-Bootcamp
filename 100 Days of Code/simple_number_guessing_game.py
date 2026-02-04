import random

random_number = random.randint(1, 100)
remaining_guesses = 0
correct_number = False


def welcome_message():
    """Starts the game off."""

    global difficulty
    global remaining_guesses
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ").lower()

    print(random_number)

    if difficulty == "easy":
        remaining_guesses = 10
    else:
        remaining_guesses = 5

    print(f"You have {remaining_guesses} chances left to guess the number.")


def play_again():
    """Function that will reset the game if player wants to play again, or not."""
    try_again = input("Would you like to play again? 'y' for yes, 'n' for no: ").lower()
    if try_again == "y":
        global correct_number
        correct_number = False
        welcome_message()
    else:
        print("Thank you for playing!")
        correct_number = True


def less_than(guess):
    """Checks if the guess is less than the random number."""
    if guess < random_number:
        global remaining_guesses
        print("Too low!")
        print("Guess again!")
        remaining_guesses -= 1
        print(f"You have {remaining_guesses} chances left to guess the number.")


def greater_than(guess):
    """Checks if the guess is greater than the random number."""
    if guess > random_number:
        global remaining_guesses
        print("Too high!")
        print("Guess again!")
        remaining_guesses -= 1
        print(f"You have {remaining_guesses} chances left to guess the number.")


def equal_to(guess):
    """Checks to see if guess is equal to the random number in order to win."""
    if guess == random_number:
        global correct_number
        print("You guessed the number!")
        correct_number = True
        play_again()


def remaining_chances(remaining_guesses):
    """Reduces the remaining chances for the player to win."""
    if remaining_guesses == 0:
        global correct_number
        print("Sorry! You did not guess the correct number!")
        correct_number = True
        play_again()


welcome_message()

while not correct_number:
    guess = int(input("Make a guess: "))
    equal_to(guess)
    less_than(guess)
    greater_than(guess)
    remaining_chances(remaining_guesses)
