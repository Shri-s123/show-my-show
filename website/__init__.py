from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy() #alchemy instance created
DB_NAME="database.db" 


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='shrishrishri'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  #add config for using sqllite db
    db.init_app(app)  #initialise say db this is the app u r used with

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User_in, Shows_onair
    from .apifetch import fetch_api1

    with app.app_context():
        db.create_all()
        # fetch_api()
        fetch_api1()


    

    login_manager=LoginManager()
    login_manager.login_view='auth.login'  #what should user see before login
    login_manager.init_app(app)

    @login_manager.user_loader  #loads user with user id
    def load_user(id):
        return User_in.query.get(str(id))

    

    return app


        