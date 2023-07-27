# flask_web_app

### Set up Directory Structure

- create a file named main.py inside a directory
- this is the file we are going to run our webServer / website
- create a folder named 'website'
- inside website folder create files:
- `__init__.py`
- auth.py
- models.py
- views.py

- `<__init__.py` ->(inside wesite folder) it is going to make the website folder a python package, which means we can import the folder, and whatever is inside the folder will run automatically once we import the folder.

### Flask setup and installation

- we are going to install a module called flask.
- this module is a super lightweight Python framework that allows you make websites really quickly and easily.

#### pip install flask

#### pip install flask-login

#### pip install flask-sqlalchemy

### Creating A Flask App

#### `__init__.py ` :

```py
from  flask import Flask
def create_app():
    app = Flask(__name__) #__name__ -> represents the name of the file
    app.config['SECRET_KEY'] = 'blahSomething'
    return app
```

```py
from flask import Flask
```

- This line imports the Flask class from the Flask module. Flask is a web framework for Python that allows you to build web applications.

```py
def create_app():
```

- This line defines a function named create_app(). This function will be used to create and configure the Flask application.

```py
 app = Flask(__name__)
```

- This line creates an instance of the Flask class and assigns it to the variable app. The `__name__` parameter is a special Python variable that represents the name of the current module. In this case, it will be the name of the file where this code is located.

```py
app.config['SECRET_KEY'] = 'blahSomething'
```

- This line sets the value of the SECRET_KEY configuration option for the Flask application. The SECRET_KEY is used for encrypting session cookies and other security-related features. It is important to keep this value secret and unique for each application.

```py
return app
```

- This line returns the created Flask application instance.

- Make sure the version of Flask you are using is compatible with the installed watchdog version.
  ` __init__.py`

##### `main.py`

```py
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

```

```py
from website import create_app
```

- This line imports the create_app function from a module named website. It assumes that there is a module named website in the current Python environment and that it contains the create_app function.

```py
app = create_app()
```

- This line calls the create_app function to create a Flask application and assigns it to the app variable. This assumes that the create_app function returns a valid Flask application instance.

```py
if __name__ == "__main__":
```

- This conditional statement checks if the current module is being executed as the main script. It ensures that the following code block is only executed when the module is run directly, rather than being imported by another module.

```py
app.run(debug=True)
```

- This line runs the Flask application using the run method. The debug=True argument enables the debug mode, which provides more detailed error messages and automatic reloading of the application when changes are made. This is useful during development but should be disabled in production.

### Creating Views and Routes

#### `views.py` :

```py
from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return "<h1>Test</h1>"

```

```py
from flask import Blueprint
```

- This line imports the Blueprint class from the Flask module. Blueprint is a way to organize routes, templates, and static files into modular components in a Flask application.

```py
views = Blueprint("views", __name__)
```

- This line creates an instance of the Blueprint class named views. The first argument, "views", is the name of the blueprint, which is used for referencing and registering the blueprint in the Flask application. The second argument, **name**, represents the name of the current module.

```py
@views.route("/")
```

- This line is a decorator that specifies the route for the following function. In this case, it decorates the home() function with the route "/". This means that when a user visits the root URL of the application, this function will be executed.

```py
def home():
```

- This line defines a function named home(). This function will be executed when a user visits the route specified by the decorator (/ in this case).

```py
return "<h1>Test</h1>"
```

- This line is the body of the home() function. It returns an HTML string `<h1>Test</h1>`, which will be sent back as the response to the user's request.

So, the overall purpose of this code is to define a blueprint named views with a single route at the root URL ("/"). When a user visits that URL, the home() function is executed, and it returns the HTML string `<h1>Test</h1>` as the response. This allows you to organize and group related routes and views in a modular manner within your Flask application.

#### `auth.py` :

```py
from flask import Blueprint

auth = Blueprint("auth", **name**)

```

```py
from flask import Blueprint
```

- This line imports the Blueprint class from the Flask module. Blueprint is a way to organize routes, templates, and static files into modular components in a Flask application.

```py
auth = Blueprint("auth", __name__)
```

- This line creates an instance of the Blueprint class named auth. The first argument, "auth", is the name of the blueprint, which is used for referencing and registering the blueprint in the Flask application. The second argument, **name**, represents the name of the current module.

So, the overall purpose of this code is to define a blueprint named auth without any routes or views. The Blueprint instance can be used to group and organize authentication-related routes, views, and other components in a modular way within a Flask application.

#### `__init__.py` :

```py
from .views import views
```

- This line imports the views blueprint from the .views module. The dot before views indicates that it is a relative import from the current package.

```py
from .auth import auth
```

- This line imports the auth blueprint from the .auth module. Similarly, it is a relative import from the current package.

```py
app.register_blueprint(views, url_prefix="/")
```

- This line registers the views blueprint with the Flask application. The url_prefix argument specifies the prefix to be added to all routes defined in the views blueprint. In this case, the routes in the views blueprint will have URLs starting with "/".

```py
app.register_blueprint(auth, url_prefix="/")
```

- This line registers the auth blueprint with the Flask application. Similarly, the url_prefix argument specifies the prefix for the routes defined in the auth blueprint.

So, the overall purpose of this code is to define a `create_app()` function that creates and configures a Flask application with two blueprints: `views` and `auth`. The blueprints are registered with the application, and the application instance is returned for further use. The blueprints can be used to organize and modularize routes and views related to different aspects of the application, such as general views and authentication views.

#### Running the webserver / App

- you can do that by just running the main.py file.

```py
python main.py
```

#### Viewing The App

Go to http://127.0.0.1:5000

#### Making more routes

```py
from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/sign-up')
def sign_up():
    return '<p>Sign Up</p>'

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'
```

```py
@auth.route('/sign-up')
```

- This line is a decorator that specifies the route for the following sign_up() function.
- It associates the URL path '/sign-up' with the sign_up() function.
- When a user visits the URL '/sign-up', the sign_up() function will be executed.

```py
def sign_up():
```

- This line defines a function named sign_up().
- This function will be executed when a user visits the route specified by the @auth.route('/sign-up') decorator.

```py
return '<p>Sign Up</p>
```

- This line is the body of the sign_up() function.
- It returns an HTML string <p>Sign Up</p>, which will be sent back as the response to the user's request when they visit the '/sign-up' URL.

- So, the overall purpose of this code is to define a blueprint named auth with three routes: '/sign-up', '/login', and '/logout'. When a user visits any of these URLs, the corresponding function will be executed, and the HTML strings will be sent back as responses to the user's request. These routes can be registered with a Flask application to handle user authentication-related functionality.
