from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/register', methods=['GET', 'Post'])
def register():
    if request.method =='post':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        return f"Registration successful for {name}{email}{password}!"
    else:
        return """"
        <h1>
         please Register
        </h1>
        <form action="/register" method="post">
        <lable>name</lable>
        <input type="text" name="name" placehoder="enter your name">
        <lable>email</lable>
        <input type="email" name="email" placehoder="enter your email">
        <lable>password</lable>
        <input type="password" name="password" placehoder="enter your password">
        <input type="submit" value="Register">
        </form>
        """
    
app.run(debug=True)
