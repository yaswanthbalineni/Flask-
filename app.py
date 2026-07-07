from flask import Flask
app= Flask(__name__)
@app.route('/course/<name>')
def course(name):
    return 'welcome to the course{name}'
@app.route('/num/<int:a>')
def num(a):
    return f' the numbers is {a}'
@app.route('/float/<float:b>')
def float(b):
    return f' the float number is {b}'
@app.route('/path/<path:c>')
def path(c):
    return f' the path is {c}'
app.route('/item/<uuid:d>')
def item(d):
    return f'the uuid is {d}'
app.run (debug=True)