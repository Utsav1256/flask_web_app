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

auth = Blueprint("auth", __name__)

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

### Creating a signUp form

#### sign_up.html

```html
{% extends 'base.html' %} {% block title %}SignUp{% endblock %} {% block content
%}
<form>
  <h3 align="center">Sign Up</h3>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input
      type="email"
      class="form-control"
      id="email"
      name="email"
      placeholder="Enter your email"
    />
  </div>
  <label for="fullName">Full Name</label>
    <input
      type="text"
      class="form-control"
      id="fullName"
      name="name"
      placeholder="Enter your full name"
    />
  </div>

</form>
{% endblock %}
```

- What the name attribute do for us??
- This is actually the attribute id going to be called when we pass the information in this feild to our backend.

### HTTP (Hypertext Transfer Protocol)

- It is the foundation of data communication on the internet.
- It is an application-layer protocol that enables communication between clients (e.g., web browsers) and servers.
- HTTP is a request-response protocol, where clients send requests to servers, and servers respond with the requested data.

#### GET:

##### Purpose:

- The GET method is used to retrieve data from the server.
- It is a safe and idempotent method, meaning that multiple identical GET requests should have the same effect as a single request.
- GET requests should not have any side effects on the server.

#### Characteristics:

- The parameters are sent in the URL's query string, which is visible in the address bar of the browser.
- The request should not have a request body (though it's technically allowed, it's rarely used in practice).

##### Common Usage:

- Retrieving web pages, images, CSS, JavaScript, and other static resources.

#### POST:

##### Purpose:

- The POST method is used to submit data to the server.
- It is not idempotent, meaning that multiple identical POST requests may have different effects on the server.
- POST requests can be used to create new resources or update existing ones on the server.

##### Characteristics:

- The data is sent in the request body, often as form data or JSON.
- The request body is not visible in the URL and is not limited in size like query parameters.

##### Common Usage:

- Submitting web forms, creating new records, uploading files.

#### PUT:

##### Purpose:

- The PUT method is used to update existing resources on the server.
- It is idempotent, meaning that multiple identical PUT requests will have the same effect as a single request.
- If the resource does not exist, the server may create it.

##### Characteristics:

- The data is sent in the request body, often as form data or JSON.
- The URL specifies the location of the resource to be updated.

##### Common Usage:

- Updating data, replacing resources.

#### DELETE:

##### Purpose:

- The DELETE method is used to delete a resource from the server.
- Like PUT, it is idempotent, meaning that multiple identical DELETE requests will have the same effect as a single request.
- If the resource does not exist, the server should typically respond with an error (e.g., 404 Not Found).

##### Characteristics:

- The URL specifies the location of the resource to be deleted.
- DELETE requests may or may not have a request body, but it's rarely used in practice.

##### Common Usage:

- Deleting resources.

#### PATCH:

##### Purpose:

- The PATCH method is used to partially update a resource on the server.
- It is similar to PUT, but while PUT replaces the entire resource, PATCH only updates specific fields or properties of the resource.

##### Characteristics:

- The data is sent in the request body, typically as a set of instructions or changes to be applied to the resource.
- The URL specifies the location of the resource to be updated.

##### Common Usage:

- Partial updates to resources.

#### HEAD:

##### Purpose:

- The HEAD method is similar to GET, but it requests only the headers of the response, not the actual data in the response body.
- It is used to check if a resource exists or to retrieve metadata about the resource without transferring the entire content.

##### Characteristics:

- The parameters are sent in the URL's query string, similar to GET.
- The response includes only the headers, without any response body.

##### Common Usage:

- Checking resource availability, getting metadata.

#### OPTIONS:

##### Purpose:

- The OPTIONS method is used to retrieve information about the communication options available for a resource on the server.
- It is used to determine the supported HTTP methods, headers, and other capabilities of the server.

##### Characteristics:

- The parameters are sent in the URL's query string, similar to GET.
- The response includes headers that provide information about the server's capabilities.

##### Common Usage:

- Determining server capabilities.

### Handling Post requests :

- We want to make sure that login and signup are able to accept post request
- To do that, we need to define something inside our root

#### auth.py

```py
@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
```

- By default it can only accept get request, but now after adding

```py
methods=["GET", "POST"]
```

it will be able to accept get and post request.

### How we get the infromation from the form on the server

- We need to import something called 'request' at the top of aur flask application.

#### auth.py

```py
from flask import Blueprint, render_template, request
```

- if we want to get the information that is sent in this form, we can do :

```py
@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
```

- Whenever you access this request variable inside of a route, it will have the information about the request that was sent to acces the route

#### login.html

```py
@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
```

Terminal(o/p):
ImmutableMultiDict([('email', 'user1@gmail.com'), ('password', '1')])

#### auth.py

```py
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if len(email) < 4:
            pass
        elif len(name) < 2:
            pass
        elif password != confirm_password:
            pass
        elif len(password) < 8:
            pass
        else:
            # add user to database
            pass
    return render_template("sign_up.html")
```

```py
def sign_up():
    if request.method == "POST":
```

```py
def sign_up():
```

- This line defines a function named sign_up().

```py
if request.method == "POST":
```

- This line checks if the HTTP request method is a POST request.
- The request object is available in Flask, and it contains information about the current HTTP request.
- In this case, the function is specifically looking for a POST request, which is usually used when submitting data to the server, like form submissions.

```py
email = request.form.get("email")
name = request.form.get("name")
password = request.form.get("password")
confirm_password = request.form.get("confirm_password")
```

- These lines retrieve data from the request's form data.
- The form data is a set of key-value pairs sent by the client (usually from an HTML form submission).
- The request.form object contains these key-value pairs, and the get() method is used to extract the values corresponding to the given keys.
- In this case, the keys are "email", "name", "password", and "confirm_password", which are the names of input fields in the HTML form.

```py
if len(email) < 4:
    pass
```

This line checks if the length of the email is less than 4 characters. If this condition is met, the code will execute the pass statement, which means it does nothing and continues to the next condition.

### Message Flashing

- We can flash a message on the screen by importing flash ( this is built in functionality in flask)

#### auth.py
```py
from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(name) < 2:
            flash("Name must be greater than 1 characters.", category="error")

        elif password != confirm_password:
            flash("Password dont't match.", category="error")

        elif len(password) < 7:
            flash("Password must be greater than 7 characters.", category="error")

        else:
            # add user to database
            flash("Account created!", category="success")
    return render_template("sign_up.html")
```
```py
 if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
```
- This line checks if the length of the email input is less than 4 characters.
- If it is, the code flashes a message with the category "error".
- Flash messages are used to display temporary messages to the user, which can be retrieved and displayed in the template.




#### base.html
```py
  <body>
    <div class="nav_bar">{% include '_navbar.html' %}</div>
    {% with messages = get_flashed_messages(with_categories=true) %} 
      {% if messages %} 
        {% for category, message in messages %} 
          {% if category == 'error' %}
            <div class="alert alert-danger alert-dismissable fade show" role="alert">
              {{message}}
              <button type="button" class="close" data-dismiss="alert">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
          {% else %}
            <div class="alert alert-success alert-dismissable fade show" role="alert">
              {{message}}
              <button type="button" class="close" data-dismiss="alert">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endwith %}
    <div class="container">{% block content %} {% endblock %}</div>
  </body>
```
- The code between '{% with %}' and '{% endwith %}' is a Jinja2 template block that handles flash messages.
- Flash messages are temporary messages that can be displayed to users after an action, like successful or failed login attempts.

```py
{% with messages = get_flashed_messages(with_categories=true) %}
```
- This line uses the get_flashed_messages function to retrieve the flashed messages.
- The with_categories=true parameter means that the messages are returned as tuples, with each tuple containing the message and its category (e.g., 'error' or 'success').
```py
{% if messages %}
```
- This line checks if there are any flashed messages. If there are, the code proceeds to loop through them to display the messages.
```py
{% for category, message in messages %}
```
- This line starts a loop to iterate over the flashed messages.
- Each message's category and content are unpacked into the variables category and message.
```py
{% if category == 'error' %}
```
- This line checks if the message category is 'error'.
- If it is, the code will display the message as a danger/alert message with a red background.
```py
{% else %}
```
- If the message category is not 'error' (i.e., it's a success message), the code will display the message as a success/alert message with a green background.
```py
{{message}}
```
- This line displays the content of the flashed message within the alert box.

```html
<button type="button" class="close" data-dismiss="alert">
    <span aria-hidden="true">&times;</span>
</button>
```
- This line adds a close button (an 'x' symbol) to the alert box, allowing users to dismiss the message.

### Flask SQLAlchemy setup

- Let's set up ur database
#### __init__.py
```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)  # __name__ -> represents the name of the file
    app.config["SECRET_KEY"] = "blahSomething"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
```

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
```
- SQLAlchemy is imported from flask_sqlalchemy, which is an extension that simplifies integration with SQL databases.

```py
db = SQLAlchemy()
```
- This line creates an instance of the SQLAlchemy class and assigns it to the variable db.
- This instance will be used to interact with the database and perform database-related operations.

```py
DB_NAME = "database.db"
```
- This line sets the name of the SQLite database file to be used as "database.db".
- This is the name of the database file that will be created when using SQLite as the database management system.

```py
def create_app():
    app = Flask(__name__)  # __name__ -> represents the name of the file
    app.config["SECRET_KEY"] = "blahSomething"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
```

```py
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
```
```py
app.config
```
- config is a dictionary-like object that holds the configuration settings for the Flask application.

```py
"SQLALCHEMY_DATABASE_URI"
```
- This is the key in the config dictionary where the database URI for SQLAlchemy is specified.
- Flask-SQLAlchemy uses this key to know where the database is located and how to connect to it.
-------
#### `URI` stands for `"Uniform Resource Identifier"`.
- It is a string of characters used to identify and locate a resource on the internet or a network.
- The resource can be anything that has a unique address, such as a web page, a file, an image, a database, or any other resource accessible over the network.

- A URI is a superset of Uniform Resource Locator (URL) and Uniform Resource Name (URN). URLs and URNs are specific types of URIs:

##### Uniform Resource Locator (URL):
- A URL is a type of URI that provides the means to locate a resource on the internet or a network.
- It includes the protocol (e.g., HTTP, HTTPS), the domain name or IP address of the server, the port number (optional), the path to the resource on the server, and any query parameters or fragments. For example, https://www.example.com:8080/page?param=value#section.

##### Uniform Resource Name (URN):
- A URN is another type of URI that provides a unique name for a resource without specifying its location.
- URNs are intended to be persistent and globally unique identifiers for resources. For example, urn:isbn:0451450523 (an ISBN number for a book).

`URIs` are used to identify and access resources in various applications, including web browsers, APIs, web services, and database connections.
- In the context of databases, like in the SQLALCHEMY_DATABASE_URI configuration parameter we discussed earlier, a URI is used to specify the connection details for the database, including the type of database (e.g., SQLite, MySQL, PostgreSQL) and its location (file path or server address).
--------
```py
f"sqlite:///{DB_NAME}"
```
- This part uses an f-string (formatted string literal) to create the database URI.
- In this case, it's using an SQLite database, so the URI starts with "sqlite://". The {DB_NAME} is the variable that holds the name of the SQLite database file, which is set as "database.db". So, the complete database URI becomes "sqlite:///database.db".
- This line sets the SQLAlchemy database URI for the SQLite database.
- The database URI tells SQLAlchemy where the database is located and how to connect to it.
- In this case, it uses SQLite as the database, and the database file will be named "database.db".

```py
db.init_app(app)
```
- This line initializes the database with the Flask application instance.
- It binds the SQLAlchemy instance (db) to the Flask app, allowing you to use SQLAlchemy features with the Flask application.