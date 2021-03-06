import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask.ext.openid import OpenID, COMMON_PROVIDERS

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = "this is a super secure key"
app.config['OPENID_PROVIDERS'] = COMMON_PROVIDERS
# remember to change to heroku's databas
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/lab5"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yzicurmnvkqqhp:Kpl-6hLvDaRcPCelsrxdmydSgi@ec2-23-21-219-209.compute-1.amazonaws.com:5432/de7vj5i2j9deb1"


db = SQLAlchemy(app)
db.create_all()
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models