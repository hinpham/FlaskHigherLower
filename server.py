from flask import Flask
from random import randint

ANSWER = randint(0, 9)
app = Flask(__name__)

def header(function):
  def wrapper():
    return f"<h1>{function()}</h1>"
  
  return wrapper


def image(function):
  def wrapper():
    return f"{function()}" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
  
  return wrapper

@app.route('/')
@header
@image
def home_page():
  return f"Guess a number between 0 and 9"


@app.route('/<int:number>')
def answer_page(number):
  if number == ANSWER:
    return f"<h1 style='color : green'>You Got It!</h1>" \
           f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
  elif number < ANSWER:
    return f"<h1 style='color : red'>Too Low!!</h1>" \
           f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
  else:
    return f"<h1 style='color : green'>You Got It!</h1>" \
           f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
  app.run(debug=True)
