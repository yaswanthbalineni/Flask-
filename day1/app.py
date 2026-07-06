from flask import Flask
app = Flask(__name__)
@app.route('/')
def Greet():
    return "hello world"
@app.route('/about')
def about():
    return "good go sand sit in the web browser"
app.run()