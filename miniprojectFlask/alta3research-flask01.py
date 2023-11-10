#!/usr/bin/python3
import starcraft
import sqlite3
import db
import logger
import gamestatus
import json
import customJSONencoder
import gameInitializer

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import send_file
from flask import session
from flask import jsonify



app = Flask(__name__)
app.secret_key = "askldjf;laksjfo83lw4yflw83y5dltuhsnd,kfjghslkdj(*^(*&TGYKHBJSDA))"

database = db.DB()
log = logger.Logger()
bad_username = False

game_initializer = gameInitializer.GameInitializer()
gamesDictionary = {}
api_not_found_error =  {'error': 'Nothing found with that name'}

def getGame():
    return gamesDictionary.get(getUsername())

def setGameStatus(username, gamestatus):
    gamesDictionary[username].gameStatus = gamestatus

def getGameStatus(username):
    if gamesDictionary.get(username):
        return gamesDictionary.get(username).gameStatus
    return None

def getUsername():
    return session.get('username')

def startNewGame(username):
    gamesDictionary[username] = starcraft.StarCraft()

# Main function
@app.route("/")
def home():
    if getGame() and getGame().are_we_dead():
        getGameStatus(getUsername()).image = "https://media3.giphy.com/media/WyrdDeIxGOlQA/giphy.gif"
    if getGame() and getGame().have_we_won():
        getGameStatus(getUsername()).image = "https://i.pinimg.com/originals/22/f9/1e/22f91e88cee06c9cc34d4da9bf1cd31d.jpg"
    return render_template("index.html", gameStatus = getGameStatus(getUsername()), 
                           won = getGame().have_we_won() if getGame() else False, 
                           gameover = getGame().are_we_dead() if getGame() else False)

# Javascript files
@app.route("/js/<name>")
def indexjs(name):
   return send_file(f"js/{name}")

# login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        data = database.login(username, password)
        if len(data) == 1:
            startNewGame(username)
            log.log("User with username: '{0}' successfully authenticated.".format(username))
            session['username'] = username
            bad_username = False
            
            return redirect(url_for('home'))
        else:
            log.log("User with username: '{0}' failed to authenticate.".format(username))
            bad_username = True
    return render_template("index.html", bad_username = bad_username)  # Create a login.html template with your login form

def run_command(command):
    setGameStatus(getUsername(), getGame().execute_command(command))

@app.route('/help')
def help():
    run_command('help')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/newgame')
def newgame():
    startNewGame(getUsername())
    return redirect(url_for('home'))

@app.route("/api/autocomplete/<text>")
def autocomplete(text):
    print("AUTOCOMPLETING")
    input_list = getGame().autocomplete(text)
    print(input_list)
    return jsonify(input_list)

@app.route("/api/command/", methods=['POST'])
def command():
    command = request.form['command']
    setGameStatus(getUsername(), getGame().execute_command(command))
    return redirect(url_for('home'))

@app.route("/api/room/<name>")
def room(name):
    room = next((obj for obj in game_initializer.rooms if obj.name.lower() == name.lower()), None)
    return jsonify(room.to_dict() if room else api_not_found_error)

@app.route("/api/rooms/")
def rooms():
    rooms = [obj.to_dict() for obj in game_initializer.rooms]
    return jsonify(rooms)

@app.route("/api/item/<name>")
def item(name):
    item = next((obj for obj in game_initializer.items if obj.name.lower() == name.lower()), None)
    return jsonify(item.to_dict() if item else api_not_found_error)

@app.route("/api/items/")
def items():
    items = [obj.to_dict() for obj in game_initializer.items]
    return jsonify(items)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug=True) # runs the application