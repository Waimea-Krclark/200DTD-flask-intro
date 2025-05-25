from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint

# Create the app
app = Flask(__name__)

# Home page - Loading static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# About page - Loading static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# Form page - Static page with a form
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')

# Handles data posted by form
@app.post("/processForm/")
def processForm():
    print(f"Form Data: ${request.form}")
    return render_template(
        'pages/number.jinja',
        name=request.form["name"],
        age=request.form["age"]
        )

# Random Number page - passing parameters to template
@app.get("/random/")
def random():
    randNum = str(randint(1,100))
    return render_template('pages/random.jinja', number = randNum)

# 404 Error - When page not found displays error
@app.errorhandler(404)
def notFound(e):
    return render_template('pages/404.jinja')

# Number Page - Getting Root value and passing to template
@app.get('/number/<int:num>')
def analyseNumber(num):
    return render_template('pages/number.jinja', number=num)