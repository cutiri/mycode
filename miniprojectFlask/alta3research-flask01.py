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

#starcraft = starcraft.StarCraft()
#gameStatus = starcraft.gameStatus
#gameStatusDict = {}
game_initializer = gameInitializer.GameInitializer()
gamesDictionary = {}
api_not_found_error =  {'error': 'Nothing found with that name'}

def getGame():
    return gamesDictionary.get(getUsername())

def setGameStatus(username, gamestatus):
    #gameStatusDict[username] = gamestatus
    #print(gamesDictionary[username].gameStatus)
    #print(gamestatus.convert_to_JSON())
    gamesDictionary[username].gameStatus = gamestatus

def getGameStatus(username):
    #return gameStatusDict.get(username)
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
    return render_template("index.html", gameStatus = getGameStatus(getUsername()))

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
            #gameStatus = starcraft.start_game()
            #setGameStatus(username, starcraft.start_game())
            print(getGameStatus(getUsername()).convert_to_JSON())
            return redirect(url_for('home'))
        else:
            log.log("User with username: '{0}' failed to authenticate.".format(username))
            bad_username = True
    return render_template("index.html", bad_username = bad_username)  # Create a login.html template with your login form

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))



@app.route("/api/autocomplete/<text>")
def autocomplete(text):
    input_list = game.autocomplete(text)
    #return { 'response': {input_list[i]: input_list[i + 1] for i in range(0, len(input_list), 2)}}
    return input_list

@app.route("/api/command/", methods=['POST'])
def command():
    command = request.form['command']
    #gameStatus = starcraft.execute_command(command)
    setGameStatus(getUsername(), getGame().execute_command(command))
    #print(getGameStatus(getUsername()).convert_to_JSON())
    return render_template("index.html", gameStatus = getGameStatus(getUsername()))

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