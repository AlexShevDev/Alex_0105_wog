import random
from utils import get_valid_number

def play(difficulty):
    random_secret_number = generate_number(difficulty)
    player_guess = get_guess_from_user(difficulty)
    return compare_results(random_secret_number, player_guess)

#Generates a random number between 0 and the specified difficulty,saving it as the secret_number.
def generate_number(difficulty):
    return random.randint(0, difficulty)

#Prompts the user to input a number within the range of 0 to the difficulty and returns the entered number.
def get_guess_from_user(difficulty):
    print(f"We started the Guess Game! Please guess a number between 0 and {difficulty}:")
    return get_valid_number(0, difficulty) # Get number from the user between 0 and difficulty


#Compares the generated secret number with the user's input and determines if they match
def compare_results(random_secret_number, player_guess):
    if random_secret_number == player_guess:
        print(f"You guessed the number! it was {random_secret_number}")
        return True
    else:
        print(f"You failed to guess the number! it was {random_secret_number}")
        return False

