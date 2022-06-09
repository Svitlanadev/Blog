from flask import Flask
# Here we are importing the Flask module and creating a Flask web server from the Flask module.
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# export FLASK_APP=blog.py
#An instance of this class Flask will be our WSGI application.

app = Flask(__name__)
# __name__ is a convenient shortcut
# Flask knows where to look for resources such as templates and static files.
login = LoginManager(app)
login.login_view='login'
# app.config.from_object(Config)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)
migrate=Migrate(app, db)
# it's migration engine
from app import routes, models


#  __name__ means this current file, in this case it will be __init__.py
#  This current file will represent my web application.
# We are creating an instance of the Flask class and calling it app.
# Here we are creating a new web application.


