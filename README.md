# World of Games

World of Games is an interactive Python-based gaming platform that offers three engaging mini-games. Players can test their memory, guessing skills, and currency conversion knowledge through these games.

## Game Description

The game starts by welcoming the player and allowing them to choose from three different games:

1. Memory Game: A sequence of numbers appears briefly, and the player must recall and input them correctly.
2. Guess Game: The player tries to guess a number chosen by the computer within a specified range.
3. Currency Roulette: Players guess the equivalent value of a USD amount in ILS (Israeli New Shekel).

Each game has adjustable difficulty levels, ranging from 1 (easiest) to 5 (hardest).

## Main Functions

### In `main.py`:
- The script initiates the game, prompting the user for a username and starting the gameplay.

### In `app.py`:
- `welcome(username)`: Displays a personalized welcome message to the player.
- `start_play()`: Presents the list of available games and manages the game selection and difficulty setting process.

### In `main_score.py`:
- `score_server()`: A Flask route that displays the player's current score.

### In `score.py`:
- `add_score(difficulty)`: Calculates and updates the player's score based on the game's difficulty.

### In `utils.py`:
- `get_valid_number(min_value, max_value)`: Ensures user inputs are valid numbers within a specified range.
- `Screen_cleaner()`: Clears the console screen (useful for the Memory Game).

### Game-specific functions:

#### In `memory_game.py`:
- `generate_sequence(difficulty)`: Creates a random sequence of numbers for the player to memorize.
- `get_list_from_user(difficulty)`: Collects the player's guess of the number sequence.
- `is_list_equal(difficulty)`: Compares the generated sequence with the player's guess.

#### In `guess_game.py`:
- `generate_number(difficulty)`: Generates a random number for the player to guess.
- `get_guess_from_user(difficulty)`: Prompts the player to make a guess.
- `compare_results(secret_number, guess)`: Checks if the player's guess matches the generated number.

#### In `currency_roulette_game.py`:
- `get_money_interval(difficulty, usd_amount)`: Calculates the acceptable range for the player's guess.
- `get_guess_from_user(difficulty, usd_amount)`: Prompts the player to guess the ILS equivalent of a USD amount.
- `compare_results(difficulty)`: Checks if the player's guess falls within the acceptable range.

Each game module also contains a `play(difficulty)` function that orchestrates the gameplay for that specific game.

The game tracks scores across multiple plays, adding challenge and replayability to the experience.

## Getting Started

To get started with World of Games, follow these steps:

1. Ensure you have Python 3.7 or later installed on your system.

2. Clone the repository to your local machine:
