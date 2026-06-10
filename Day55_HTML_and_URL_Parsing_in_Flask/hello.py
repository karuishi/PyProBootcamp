from flask import Flask
from markupsafe import escape

app = Flask(__name__) # special attribute, in this case: __name__ == __main__

# Python decorator. This one only allows the mehtods to trigger if the user is acessing the home page url ('/')
@app.route('/') 
def hello_world():
    return "Hello, World!"

# Different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "Bye"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you're {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)