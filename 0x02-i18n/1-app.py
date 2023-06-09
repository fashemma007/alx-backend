#!/usr/bin/env python3
"""module docs for 1-app.py"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """application configurations"""
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # load configurations
# print(app.config)  # see all configs
babel = Babel(app)


@app.route("/")
def index():
    """Homepage"""
    results = {"title": "Welcome to Holberton", "header": "Hello world"}
    return render_template("1-index.html", results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
