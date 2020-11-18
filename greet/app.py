from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns Welcome page"""
    return '<h1>Welcome</h1>'

@app.route('/welcome/home')
def home():
    """Returns Welcome Home page"""
    return '<h1>Welcome Home</h1>'

@app.route('/welcome/back')
def back():
    """Returns Welcome Back page"""
    return '<h1>Welcome Back</h1>'