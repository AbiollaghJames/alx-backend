#!/usr/bin/env python3
"""
Get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


#@babel.localeselector
def get_locale() -> str:
    """determine the best match lang"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """ Home/Index page """
    return render_template('3-index.html')


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(debug=True)
