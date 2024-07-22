import random
import time
from utils import Screen_cleaner

def play(difficulty):
    return is_list_equal(difficulty)

def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    print(random_list)
    time.sleep(0.7)
    Screen_cleaner() # Function from utils
    return random_list

def get_list_from_user(difficulty):
    while True:
        player_guess = input(f"We started the Memory Game! Guess the {difficulty} numbers you just saw, separated by commas: ")
        guess_list_str = player_guess.split(',') # Split the string into a list of strings using commas as separators
        for i in range(len(guess_list_str)): # Remove whitespace from each string
            guess_list_str[i] = guess_list_str[i].strip()

        if len(guess_list_str) != difficulty:
            print(f"You need to enter {difficulty} numbers!")
            continue

        # Convert the list of strings to a list of integers
        guess_list_int = []
        for num in guess_list_str:
            if not num.isdigit():
                print("Please enter only numbers separated by commas!")
                break
            guess_list_int.append(int(num))
        else:
            all_valid = True
            for num in guess_list_int:
                if not (1 <= num <= 101):
                    all_valid = False
                    break

            if all_valid:
                return guess_list_int
            else:
                print("One or more numbers are out of the valid range (1-101)")


def is_list_equal(difficulty):
    random_list = generate_sequence(difficulty)
    list_of_player_guess = get_list_from_user(difficulty)
    if random_list == list_of_player_guess:
        print("You guessed the numbers!")
        return True
    else:
        print(f"You failed to guess the numbers! the answer was {random_list}")
        return False

