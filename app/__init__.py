# from flask - flask package
# import Flask - class Flask
# app = .. an instance of class Flask
from flask import Flask

# export FLASK_APP=blog.py
#An instance of this class Flask will be our WSGI application.

app = Flask(__name__)  #create an instance
app.config.from_pyfile('config.py')
from app import routes


# routes module
# There are two entities named app
# The app package is defined by the app directory and the __init__.py script,
# and is referenced in the from app import routes statement.
# The app variable is defined as an instance of class Flask in the __init__.py script,
# which makes it a member of the app package.

