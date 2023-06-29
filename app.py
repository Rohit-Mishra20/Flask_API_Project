from flask import Flask 

app =  Flask(__name__)

@app.route("/")
def home():
    return "Server is running, to view the data /metrics"

from metrics_controller import *