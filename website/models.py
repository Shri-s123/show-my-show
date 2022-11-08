from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import uuid





class User_in(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key=True,default= lambda : str(uuid.uuid4()))
    email= db.Column(db.String(150), unique=True, nullable=False)
    firstname = db.Column(db.String(150), unique=False, nullable=False)
    lastname = db.Column(db.String(150), unique=False, nullable=False)
    username = db.Column(db.String(150), unique=False, nullable=False)
    password = db.Column(db.String(150), unique=False, nullable=False)
    interests= db.Column(db.String(150), unique=False, nullable=False)





class Shows_onair(db.Model):
    id = db.Column(db.String(150), primary_key=True,default= lambda : str(uuid.uuid4()))
    showid = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=False)
    genres= db.Column(db.String(150), unique=False, nullable=False)
    image = db.Column(db.String(150), unique=False, nullable=False)
    language = db.Column(db.String(150), unique=False, nullable=True)
    rating = db.Column(db.String(150), unique=False, nullable=True)
    summary = db.Column(db.String(150), unique=False, nullable=True)


class user_shown(db.Model):
    id = db.Column(db.String(150), primary_key=True,default= lambda : str(uuid.uuid4()))
    user_email= db.Column(db.Integer, unique=False, nullable=False)
    shows_list= db.Column(db.String(300), unique=False, nullable=False)


    




    
    

