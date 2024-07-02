from currency_roulette_game import play as crg_play
from guess_game import play as gg_play
from memory_game import play as mm_play
from utils import get_valid_number
from score import add_score
from main_score import score_server
#This function takes a person's name as input and displays a personalized welcome message
def welcome(username):
    print(f"\nHi {username} and welcome to the World of Games: The Epic Journey")

#This function presents a list of available games to the user
def start_play():
    print("""
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")
    #game_user_choice = input("Your choice is: ")
    valid_game_user_choice = get_valid_number(1, 3)

    print("Select a difficulty level between 1 (easiest) and 5 (hardest):")
    #difficulty_user_choice = input("Your choice is: ")
    valid_difficulty_user_choice = get_valid_number(1, 5)


    if valid_game_user_choice == 1:
        # Memory Game
        game_result = mm_play(valid_difficulty_user_choice)
    elif valid_game_user_choice == 2:
        # Guess Game
        game_result = gg_play(valid_difficulty_user_choice)
    elif valid_game_user_choice == 3:
        # Currency Roulette Game
        game_result = crg_play(valid_difficulty_user_choice)

    if game_result: # Value should return True
        add_score(valid_difficulty_user_choice)


