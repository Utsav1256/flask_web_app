# flask_web_app

### Set up Directory Structure

- main.py -> this is the file we are going to run our webServer / website
- <!--  __init__.py --> ->(inside wesite folder) it is going to make the website folder a python package, which means we can import the folder, and whatever is inside the folder will run automatically once we import the folder.

### Flask setup and installation

- we are going to install a module called flask.
- this module is a super lightweight Python framework that allows you make websites really quickly and easily.

#### pip install flask

#### pip install flask-login

#### pip install flask-sqlalchemy

### Creating A Flask App

#### <!-- __init__.py --> :

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

- This line creates an instance of the Flask class and assigns it to the variable app. The <!-- __name__ --> parameter is a special Python variable that represents the name of the current module. In this case, it will be the name of the file where this code is located.

```py
app.config['SECRET_KEY'] = 'blahSomething'
```

- This line sets the value of the SECRET_KEY configuration option for the Flask application. The SECRET_KEY is used for encrypting session cookies and other security-related features. It is important to keep this value secret and unique for each application.

```py
return app
```

- This line returns the created Flask application instance.

- Make sure the version of Flask you are using is compatible with the installed watchdog version.
<!-- __init__.py -->

##### main.py

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
