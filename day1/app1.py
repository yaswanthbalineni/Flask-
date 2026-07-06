from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "welcome home"

@app.route('/about/<name>')
def about(name):
    return F"hello is the name of the person {name}"

@app.route('/add/<a>/<b>')
def add(a,b):
    return f"the sum of the numbers are {a} and {b} is {a+b}"
app.run(debug=True)