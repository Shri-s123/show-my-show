from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Shows_onair, User_in, user_shown
from . import db

views=Blueprint('views',__name__)

@views.route('/',methods=['GET'])
@login_required
def home():
    user_email=request.cookies.get('user_email')
    user= User_in.query.filter_by(email=user_email).first()
    shows = Shows_onair.query.filter_by(genres=user.interests)
    
    new_shows=[]   
    n=0 
    for show in shows:
        
        shown= user_shown.query.filter_by(user_email=user_email,shows_list=str(show)).first()
        if shown:
            continue
        else:
            new_shows.append(show)
            user_shown_obj=user_shown(user_email=user_email,shows_list=str(show))
            db.session.add(user_shown_obj)
            db.session.commit()
            n+=1
            if n==5:
                break
    
    shows=new_shows
    
    return render_template("home.html",user=current_user, shows=shows) 


@views.route('/reset',methods=['GET','POST'])
@login_required
def reset():
    user_email=request.cookies.get('user_email')
    data=user_shown.query.filter_by(user_email=user_email)
    for record in data:
        db.session.delete(record)
        db.session.commit()
    flash('Recommendations History Reset Successful!',category='success')

    return redirect(url_for("views.home"))


    
