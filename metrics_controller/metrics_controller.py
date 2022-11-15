from app import app
from model.matrics_model import matrics_model_class
from flask import request

obj=matrics_model_class()

@app.route("/metrics")
def metrics():
    return obj.get_matrics_data_model(request.args)

@app.route("/metrics",methods=["POST"])
def post_metrics():
    return obj.post_matrics_data_model(request.form)