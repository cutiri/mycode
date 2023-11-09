#!/usr/bin/python3
import starcraft
import sqlite3

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import send_file
from flask import session


app = Flask(__name__)
game = starcraft.StarCraftRPG()

# Main function
@app.route("/")
def hello_world():
   return render_template("index.html")

# Javascript files
@app.route("/js/<name>")
def indexjs(name):
   return send_file(f"js/{name}")

# login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']

        if username == dummy_user['username'] and password == dummy_user['password']:
            session['username'] = username
            return redirect(url_for('home'))

        return 'Invalid login credentials'

    return render_template('login.html')  # Create a login.html template with your login form




@app.route("/api/autocomplete/<text>")
def autocomplete(text):
    input_list = game.autocomplete(text)
    #return { 'response': {input_list[i]: input_list[i + 1] for i in range(0, len(input_list), 2)}}
    return input_list

@app.route("/api/command/<text>")
def command(text):
   pass


if __name__ == "__main__":
   
   app.run(host="0.0.0.0", port=2224, debug=True) # runs the application