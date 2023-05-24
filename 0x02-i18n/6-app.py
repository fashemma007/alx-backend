#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as', None)  # get user id
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    # [print(param) for param in request.args.lists()]
    # get the locale param from the request url
    locale = request.args.get("locale", None)
    user = g.user  # user session
    header_locale = request.headers.get('locale', None)  # header locale

    if locale is None and user:
        # get locale from user's login
        locale = g.user.get('locale')
    elif locale is None and header_locale:
        locale = header_locale

    if locale in app.config["LANGUAGES"]:  # chk for availability
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
