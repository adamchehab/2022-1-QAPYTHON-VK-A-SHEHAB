#! /usr/bin/env python3.8

import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


app_data = {}
user_id_seq = 1


@app.route("/add_user", methods=["POST"])
def create_user():
    global user_id_seq

    user_name = json.loads(request.data)["name"]
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        user_id_seq += 1
        return jsonify({"user_id": app_data[user_name]}), 201

    else:
        return jsonify(f"User already created, user ID= {app_data[user_name]}"), 400


@app.route("/get_user/<name>", methods=["GET"])
def get_user(name):
    if user_id := app_data.get(name):
        return jsonify({"user_id": user_id}), 200
    else:
        return jsonify(f"User not found {name}"), 404


if __name__ == "__main__":
    host = os.environ.get("APP_HOST", "127.0.0.1")
    port = os.environ.get("APP_POST", "5000")

    app.run(host, port)
