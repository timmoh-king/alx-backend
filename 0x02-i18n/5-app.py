#!/usr/bin/env python3

"""
    implement a way to force a particular locale by passing the locale=fr
    parameter to your app’s URLs.
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional, Dict


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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict, None]:
    """
         if the ID cannot be found or if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request() -> None:
    """set user as a global on flask.g.user."""
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """
        In your get_locale function, detect if the incoming request contains
        locale argument and ifs value is a supported locale, return it
        If not or if the parameter is not present return default
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))

    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """render the 1-index.html page once the route is given"""
    return render_template('5-index.html')


if __name__ == '__main__':
    """The app will be accessible at http://localhost:5000"""
    app.run(host='0.0.0.0', port=5000)
