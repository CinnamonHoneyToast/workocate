# import the nessecary pieces from Flask
from flask import Flask, render_template, request, jsonify, Response, request
from flaskext.mysql import MySQL

#Create the app object that will route our calls
app = Flask(__name__)

# Add a single endpoint that we can use for testing
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

