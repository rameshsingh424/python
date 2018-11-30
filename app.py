#!C:\Users\ramesh\AppData\Local\Programs\Python\Python37-32/python.exe
from flask import Flask, render_template
app = Flask(__name__)

#server = app.server

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)