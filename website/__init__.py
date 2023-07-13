from flask import Flask


def create_app():
    app = Flask(__name__)  # __name__ -> represents the name of the file
    app.config["SECRET_KEY"] = "blahSomething"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
