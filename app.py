from flask import Flask
from flask import request
from markupsafe import (
    escape,
)  # Escape all user input. Jinja templates do it automatically

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = request.args.get("name", "Flask")
    return f"<p>Hello, {escape(name)}!</p>"


if __name__ == "__main__":
    app.run(debug=True)
