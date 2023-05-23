#!/usr/bin/env python3
"""module docs for 1-app.py"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """application configurations"""
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # load configurations
# print(app.config)  # see all configs
babel = Babel(app)


@app.route("/")
def index():
    """Homepage"""
    results = {"Hello world"}
    return render_template("1-index.html", results=results)


if __name__ == "__main__":
    app.run()
