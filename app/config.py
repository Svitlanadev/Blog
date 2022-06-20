from app import app
import os
basedir= os.path.abspath(os.path.dirname(__file__))


app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['POSTS_PER_PAGE'] = 5

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'GDtfDCFYjD'
#     SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     POSTS_PER_PAGE = 3

