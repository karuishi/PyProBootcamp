from flask import Flask

app = Flask(__name__) # special attribute, in this case: __name__ == __main__

@app.route('/') # Python decorator. This one only allows the mehtods to trigger if the user is acessing the home page url ('/')
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()