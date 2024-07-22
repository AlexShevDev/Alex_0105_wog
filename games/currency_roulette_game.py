# https://freecurrencyapi.com/docs/#authentication-methods
# https://app.freecurrencyapi.com/dashboard
# https://pypi.org/project/CurrencyConverter/

from currency_converter import CurrencyConverter
import random
import requests


def play(difficulty):
    return compare_results(difficulty)

def get_money_interval(difficulty, rand_number_in_usd):
    # Getting the currency from freecurrencyapi
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_Fa9zx8ZMrUiSr2a1LrffJLy8PiqwgAfnCAQZIrIa"
    resp = requests.get(url)
    if resp.status_code == 200: # API successful
        data = resp.json()
        ils_value = data["data"]["ILS"]
        rand_number_in_ils = rand_number_in_usd * float(ils_value)
        allowed_difference = 10 - difficulty
        return allowed_difference, rand_number_in_ils

    else: # API failed so use offline currency converter
        #print(f"Error: API request failed with status code {resp.status_code}")
        print("We have some connection issues, so we will use offline currency converter")
        currency_data = CurrencyConverter()
        rand_number_in_ils = currency_data.convert(rand_number_in_usd, 'USD', 'ILS')  # Convert from USD to ILS
        allowed_difference = 10 - difficulty
        return allowed_difference, rand_number_in_ils


def get_guess_from_user(difficulty, rand_number_in_usd):
    while True:
        player_guess_char = input(f"We started the Currency Roulette game! Guess the value of {rand_number_in_usd} USD converted to ILS: ")
        try:
            player_guess_num = float(player_guess_char)
            return player_guess_num
        except:
            print("Please choose a valid number")

def compare_results(difficulty):
    rand_number_in_usd = random.randint(1, 100)
    allowed_difference, rand_number_in_ils = get_money_interval(difficulty, rand_number_in_usd)
    player_guess = get_guess_from_user(difficulty, rand_number_in_usd)

    if (rand_number_in_ils - allowed_difference) <= player_guess <= (rand_number_in_ils + allowed_difference):
        print(f"You guessed within the range! the answer was {round(rand_number_in_ils, 2)} ILS")
        return True
    else:
        print(f"You FAILED to guess the value! the answer was {round(rand_number_in_ils, 2)} ILS")
        return False

