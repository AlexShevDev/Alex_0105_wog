from os import system

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = -999

# A function to check if the number is valid (not char, or out of range)
def get_valid_number(min_value, max_value):
    while True:
        user_input = input(f"Please enter a number: ")
        if user_input.isdigit():
            number = int(user_input)
            if min_value <= number <= max_value:
                return number
                break
            else:
                print(f"The number should be between {min_value} and {max_value}!")
        else:
            print("Please enter a valid number!")


# A function to clear the screen (useful when playing memory game or before a new game starts)
def Screen_cleaner():
    system('cls')