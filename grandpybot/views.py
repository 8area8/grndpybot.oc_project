"""Main file for views."""

from flask import render_template, request, jsonify

from grandpybot import app
from grandpybot.api_requests import request_google_place, request_media_wiki
from grandpybot.parser import Parser


@app.route('/index/')
@app.route('/')
def index():
    """Return the main file."""
    key = app.config["GOOGLE_KEY"]
    url = ("https://maps.googleapis.com/maps/"
           f"api/js?key={key}&callback=initMap")

    return render_template('index.html', url_map_api=url, title="Home")


@app.errorhandler(404)
def not_found(error):
    """If 404 error."""
    return (render_template('404.html', title="404"), 404)


@app.errorhandler(500)
def internal_error(error):
    """If 500 error."""
    return (render_template('500.html', title="500"), 500)


@app.route('/about/')
def about():
    """Return the about file."""
    return render_template('about.html', title="Qui suis-je ?")


@app.route('/api_request', methods=['GET', 'POST'])
def place_request():
    """Send request to Google place API and Media Wiki API.

    Return the response.
    """
    user_input = request.form["data"]
    parsed_input = Parser.parse(user_input)

    google_response = request_google_place(parsed_input)
    wiki_response = {}

    if google_response["status"] == "OK":
        wiki_response = request_media_wiki(google_response["coords"], google_response["name"])

    return jsonify({**google_response, **wiki_response})


@app.after_request
def add_header(req):
    """Add headers to both force latest IE rendering engine or Chrome Frame.

    Also to cache the rendered page for 10 minutes.
    """
    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
