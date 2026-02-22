"""https://flask.palletsprojects.com/en/stable/quickstart/"""

from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    """root"""
    return "This is the index page"


@app.route("/hello")
def hello_world():
    """
    Minimal sample. Response to /hello
    With optional ?name
    """
    name = request.args.get("name", "Flask")
    # Escape all user input. Jinja templates do it automatically
    return f"<p>Hello, {escape(name)}!</p>"


if __name__ == "__main__":
    app.run(debug=True)
