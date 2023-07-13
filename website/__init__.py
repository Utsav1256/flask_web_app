from flask import Flask


def create_app():
    app = Flask(__name__)  # __name__ -> represents the name of the file
    app.config["SECRET_KEY"] = "blahSomething"
    return app
