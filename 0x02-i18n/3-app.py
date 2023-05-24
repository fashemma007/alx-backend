#!/usr/bin/env python3
"""module docs for 1-app.py"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    """application configurations"""
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # load configurations
# print(app.config)  # see all configs
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return 'fr'
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Homepage"""

    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
