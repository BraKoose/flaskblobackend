from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config ['SECRET_KEY']= '9eac60dbf293a5700d07fb2fb8015bfba2217b6fb60b7443f399442a9a6bec55'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db= SQLAlchemy(app)
bcrypt= Bcrypt(app)

from flaskblog import routes