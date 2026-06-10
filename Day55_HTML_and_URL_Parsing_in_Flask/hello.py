from flask import Flask

app = Flask(__name__) # special attribute, in this case: __name__ == __main__

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

# Python decorator. This one only allows the mehtods to trigger if the user is acessing the home page url ('/')
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
            '<p>This is a paragraph.</p>'\
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjA3ZzEwajE2d2MwemR2Znk4NXY3djV5ODIyY2xncWZwbXowdG9qdSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/7G70mmE4fQYJDlZtEr/giphy.gif" width=200s>'

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined 
def say_bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you're {number} years old!"

if __name__ == "__main__": 
    app.run(debug=True)