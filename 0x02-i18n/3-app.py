#!/usr/bin/env python3

"""
    Use the _ or gettext function to parametrize your templates
    Use the message IDs home_title and home_header.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
        Create a get_locale function with the babel.localeselector decorator
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Create a get_locale function with the babel.localeselector"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """render the 1-index.html page once the route is given"""
    return render_template('2-index.html')


if __name__ == '__main__':
    """The app will be accessible at http://localhost:5000"""
    app.run(host='0.0.0.0', port=5000)
