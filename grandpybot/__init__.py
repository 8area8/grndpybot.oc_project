"""Flask init."""

from flask import Flask


app = Flask(__name__)
app.config.from_object('flaskenv.conf')

from grandpybot import views
