#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. Responds to HTTP 'GET /' requests
   with a 'Hello World' attached to a 200 response"""


# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/home")
def home():
   return "Home page"

@app.route("/json")
def json():
   return {"name": "Angel", "lastname": "Villasante"}

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug=True) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
