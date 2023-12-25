from flask import Flask
import random

app = Flask(__name__)

rand_number = random.randint(0, 9)

@app.route("/")
def index():
    return "<h1>Guess a number between 0 to 9</h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>" 

@app.route('/<int:number>')
def check_number(number):
    if number < rand_number:
        return f"<h2 style='color: red'>{number} is too low</h2> <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    elif number > rand_number:
        return f"<h2 style='color: purple'>{number} is too high</h2> <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    else:
        return f"<h2 style='color: green'>Correct</h2> <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"

if __name__ == '__main__':
    app.run(debug=True)