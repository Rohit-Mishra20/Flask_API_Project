from app import app
from model.matrics_model import matrics_model_class
from flask import request
import json

obj=matrics_model_class()

@app.route("/metrics")
def metrics():
    return obj.get_matrics_data_model(request.args)

@app.route("/metrics",methods=["POST"])
def post_metrics():
    try:
        data=request.get_json()
        return obj.post_matrics_data_model(data)
    except Exception as e:
        return "Post request can not be made, due to issue: Please check the body it should be in json format: "+str(e)