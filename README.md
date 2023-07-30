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

### Rendering Pages

#### Create a base template (aka layout)

#### base.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>{% block title %}Default{% endblock %}</title>
  </head>
  <body>
    <div class="nav_bar">{% include '_navbar.html' %}</div>
    <div class="container">{% block content %} {% endblock %}</div>
  </body>
</html>
```

```html
<title>{% block title %}Default{% endblock %}</title>
```

- This line defines a block named title with a default value of "Default".
- It will be replaced with specific values from child templates that extend this base template.

```html
<div class="nav_bar">{% include '_navbar.html' %}</div>
```

- This line includes the content from \_navbar.html inside a div with the class nav_bar.
- The include directive is used to insert the content from another template into this template.

```html
<div class="container">{% block content %} {% endblock %}</div>
```

- The content within this block will be replaced by specific content from child templates that extend this base template.

#### home.html

```html
{% extends 'base.html' %} {% block title %}Home{% endblock %} {% block content
%}
<h1>This is the Home page.</h1>
{% endblock %}
```

```html
{% extends 'base.html' %}
```

- This line indicates that home.html is extending the base.html template, so it will inherit its structure and blocks.

```html
{% block title %}Home{% endblock %}
```

- This line overrides the title block from the base.html template.
- It sets the title to "Home" for this specific page.

```html
{% block content %} and {% endblock %}
```

- These lines define the content block for this template. The content within this block will replace the content block in the base.html template.

#### login.html

```html
{% extends 'base.html' %} {% block title %}Login{% endblock %} {% block content
%}
<h1>This is the Login page.</h1>
{% endblock %}
```

- The login.html template follows a similar structure to home.html, but the title and content are specific to the Login page.

#### signup.html

```html
{% extends 'base.html' %} {% block title %}SignUp{% endblock %} {% block content
%}
<h1>This is the SignUp page.</h1>
{% endblock %}
```

- The signup.html template is also similar in structure, but the title and content are specific to the SignUp page.

- In summary, these templates use Flask's templating engine (Jinja2) to create reusable components (base.html) that can be extended and overridden by child templates (home.html, login.html, signup.html). The extends directive allows child templates to inherit the structure and blocks from the base template, and the block and endblock directives define the areas where the content can be replaced. This templating approach makes it easier to maintain and organize the HTML code for different pages in a Flask application.

#### auth.py

```py
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'
```

```py
from flask import Blueprint, render_template
```

- This line imports the Blueprint class and the render_template function from Flask.
- Blueprint is used to organize routes,
- and render_template is used to render HTML templates.

```py
auth = Blueprint("auth", __name__)
```

- This line creates an instance of the Blueprint class named auth.
- The first argument, "auth", is the name of the blueprint, which is used for referencing and registering the blueprint in the Flask application.
- The second argument, **name**, represents the name of the current module.

```py
@auth.route('/sign-up')
```

- This line is a decorator that specifies the route for the following sign_up() function.
- It associates the URL path '/sign-up' with the sign_up() function.
- When a user visits the URL /sign-up, the sign_up() function will be executed.

```py
def sign_up()
```

- This line defines a function named sign_up().
- This function will be executed when a user visits the route specified by the @auth.route('/sign-up') decorator.

```py
return render_template('sign_up.html')
```

- This line uses the render_template function to render the sign_up.html template.
- The rendered HTML content will be sent back as the response to the user's request when they visit the /sign-up URL.

```py
@auth.route('/login')
```

- This line is a decorator that specifies the route for the following login() function.
- It associates the URL path '/login' with the login() function.
- When a user visits the URL /login, the login() function will be executed.

```py
def login():
```

- This line defines a function named login().- This function will be executed when a user visits the route specified by the
  @auth.route('/login') decorator.

```py
return render_template('login.html')
```

- his line uses the render_template function to render the login.html template.
- The rendered HTML content will be sent back as the response to the user's request when they visit the /login URL.

- Similarly, the logout.

### Passing a variable to templates and display it on the page

#### auth.py

```py
@auth.route("/login")
def login():
    return render_template("login.html", text="Testing", user="Utsav")
```

#### login.html

```html
{% extends 'base.html' %} {% block title %}Login{% endblock %} {% block content
%}
<h1>This is the Login page.</h1>
{{text}} {{user + 's'}} {% endblock %}
```

- So there is a limitation what you can do inside '{{here}}'.
- You can't do can't do everything you do in regular python.
- But for the most part you can use like some basic expressions, display variables.

### Use if statement in a template

#### auth.py

```py
@auth.route("/login")
def login():
    return render_template("login.html", boolean=True)
```

#### login.html

```html
{% extends 'base.html' %} {% block title %}Login{% endblock %} {% block content
%}
<h1>This is the Login page.</h1>
{% if boolean == True %} Yes it is true! {% endif %} {% endblock %}
```

### if else

#### login.html

```html
{% extends 'base.html' %} {% block title %}Login{% endblock %} {% block content
%}
<h1>This is the Login page.</h1>
{% if boolean == False %} Yes it is true! {% else %} No it is not true {% endif
%}{% endblock %}
```
