#!/usr/bin/env python3
"""
Get locale from request
"""

from typing import Union, Dict
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Config class'''

    DEBUG = True
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
    """
    function that returns a user dictionary
    or None if the ID cannot be found or if
    login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
     executed before any function
     use get_user to find a user if any
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Gets the locale for page.
    """
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    locale_h = request.headers.get('locale', '')
    if locale_h in app.config["LANGUAGES"]:
        return locale_h
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """Home route"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
