# src/__init__.py

import os
from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


@app.route("/")
def main():
    return "Hello"


@app.route("/ping")
def ping():
    return {
        "message": "pong!",
        "status": "success"
        }