from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response
from .models import *
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data =request.form
    if request.method == 'POST':
        email= request.form.get('email')
        password= request.form.get('password')
        user = User_in.query.filter_by(email=email).first()
        if user :
            if password and check_password_hash(user.password,password):
                flash('Loggin successful',category='success')
                login_user(user, remember=True)
                
                user_email=user.email
                resp=make_response(redirect(url_for("views.home")))
                resp.set_cookie('user_email',user_email)
                return resp
                

                
            else:
                flash('IncorrectPassword. Retry login',category='error')
        else:
            flash('User doesn\'t exist', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    data=request.form
    if request.method == 'POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        v=password1
        interests=request.form.get('interests')


        user = User_in.query.filter_by(email=email).first()
        
        if user:
            flash('Email is already registered with a different user.',category='error')
        elif len(email)<4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstname)<3:
            flash('Firstname must be greater than 2 characters', category='error')
        elif len(lastname)<1:
            flash('Lastname cannot be less than 1 character', category='error')
        elif len(username)==0:
            flash('Username cannot be empty',category='error')
        elif len(password1)==0 or len(password2)==0:
            flash('Password cannot be null',category='error')
        elif password1!=password2:
            flash('Passwords don\'t match', category='error')
        
        elif len(password1)<7: #v=password1 for ease
            flash("The password is weak", category='error')

        
        else :
            user_obj=User_in(email=email,firstname=firstname,lastname=lastname,username=username,password=generate_password_hash(password1, method='sha256'),interests=interests)
            db.session.add(user_obj)
            db.session.commit()
            flash('Account setup successful!',category='success')
            login_user(user_obj, remember=True)  #hols user data during session ..remembers till browsing history deleted or server reruns
            
            user_email= user_obj.email
            resp=make_response(redirect(url_for("views.home")))
            resp.set_cookie('user_email',user_email)
            return resp


    return render_template('signup.html', user=current_user)

    