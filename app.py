from flask import Flask 

app =  Flask(__name__)

@app.route("/home")
def home():
    return "API home path"

from metrics_controller import *