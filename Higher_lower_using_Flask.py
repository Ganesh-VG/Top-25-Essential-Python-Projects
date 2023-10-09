from flask import Flask
import random
app = Flask(__name__)

rand = random.randint(0,9)

@app.route('/')
def guess():
    return "<h1> Guess a number between 0 and 9 </h1>"\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>'


@app.route("/<int:num>")
def greet(num):
    if num > rand:
        return "<h1> Number is too high </h1>"\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>'
    elif num < rand:
        return "<h1> Number is too low </h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>'
    elif num == rand:
        return "<h1> You got it </h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'
    else:
        return "<h1> Out of range </h1>"



if __name__ == "__main__":
    app.run(debug=True)