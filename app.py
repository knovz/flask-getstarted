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


# Routes with vars
@app.route("/user/<username>")
def show_user_profile(username):
    """route with variable"""
    return f"User: {escape(username)}"


# Id the param is not an int, it will not use this route.
# If there is another route /post/str: it will use the mathching one
# depending on the post_id type
@app.route("/post/<int:post_id>")
def show_post(post_id):
    """route with converted variable"""
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    """route with path conversion"""
    return f"Subpath {escape(subpath)}"


# Type conversions
# string | (default) accepts any text without a slash
# int    | accepts positive integers
# float  | accepts positive floating point values
# path   | like string but also accepts slashes
# uuid   | accepts UUID strings

# Trainling slashes
# /projects/
# /about
# If the user types /projects it will be redirected to /projects/
# If the user types /about/ it will be "not found"


if __name__ == "__main__":
    app.run(debug=True)
