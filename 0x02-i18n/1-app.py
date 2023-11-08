#!/usr/bin/env python3

"""
    Use Config to set Babel’s default locale ("en") and timezone ("UTC").
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
        set LANGUAGES class attribute equal to ["en", "fr"].
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """render the 1-index.html page once the route is given"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """The app will be accessible at http://localhost:5000"""
    app.run(host='0.0.0.0', port=5000)
