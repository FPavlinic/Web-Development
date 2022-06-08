# used libraries
from flask import Flask
from random import randint

# create Flask object
app = Flask(__name__)

# home page
@app.route('/')
def higher_lower_home():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>"

# insert number in url after '/' to make a guess
@app.route('/<int:number>')
def higher_lowe_game(number):
    random_number = randint(0, 9)

    # display different gifs in browser depending on the guess
    if number < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if number > random_number:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if number == random_number:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


# run web app
if __name__ == "__main__":
    app.run(debug=True)
