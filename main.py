from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def home():
    return " Hello World"

@app.route('/index')
def index():
    return render_template('index.htlm')

# def index():
#     return "This is my home page"

@app.route('/myname')

def myname():
    return "I am Bina."


app.run(debug=True)

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    age = request.form['age']
    db=request.form['dateofbirth']
    print(name)
    return render_template('pass.html', n=name, age=age, db=db)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# db=SQLAlchemy(app)


def decor(printer):
    def inner():
        printer()
        print("welcome")
    return inner

@decor
def printer():
    print("Hi")
    print("Hi")
printer()






