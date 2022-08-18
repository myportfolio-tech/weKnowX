# src/__init__.py

import os
import sys
from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


# print(app.config, file=sys.stderr)

@app.route("/")
def main():
    return "Hello"


@app.route("/ping")
def ping():
    return {
        "message": "pong!",
        "status": "success"
        }