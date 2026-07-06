from flask import Flask,redirect
app = Flask(__name__)
@app.route('/')
def home():
    return "welcome to home page"

@app.route('/about')
def about():
    return redirect('/')
app.run(debug=True)