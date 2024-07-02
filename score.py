from utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    try:
        score_file = open(SCORES_FILE_NAME, "r+")
        player_points = int(score_file.read())
    except: # If not able to read from default file
        score_file = open(SCORES_FILE_NAME, "x")
        player_points = 0

    player_points += POINTS_OF_WINNING(difficulty) # Calculate new amount of points
    score_file.seek(0)  # Move pointer to the beginning of the file
    score_file.write(str(player_points)) # Write into file
    score_file.close()

# add_score(2)