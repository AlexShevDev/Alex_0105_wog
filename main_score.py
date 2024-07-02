from flask import Flask, render_template
from utils import SCORES_FILE_NAME
# https://pypi.org/project/Flask/
# https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        score_file = open(SCORES_FILE_NAME, "r+")
        player_points = int(score_file.read())
        return render_template("score.html", SCORE=player_points)
    except:
        return render_template("score_error.html")


if __name__ == '__main__':
    app.run(port=8000)  # Run Flask port 8000
