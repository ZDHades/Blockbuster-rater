from .import bp as authentication
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, current_user, login_required, logout_user
from .forms import Register, Login
from .models import User

@authentication.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()

    if form.validate_on_submit():
        data = {
            'first_name' : request.form.get('first_name'),
            'last_name' : request.form.get('last_name'),
            'email' : request.form.get('email'),
            'password' : request.form.get('password')
        }
        u = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])

        u.hash_pass(u.password)

        db.session.add(u)
        db.session.commit()

        flash("You have successfully registered!", 'primary')

        return redirect(url_for('authentication.login'))

    content = {
        'form' : form
    }

    return render_template('register.html', **content)

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    
    user = User.query.filter_by(email=request.form.get('email')).first()
    if form.validate_on_submit():
        if user is None or not user.check_password(request.form.get('password')):
            flash("You have entered incorrect details, please try again", 'danger')
            return redirect(url_for('authentication.login'))
        login_user(user)
        flash("You have successfully logged in!", 'success')
        return redirect(url_for('main.index'))
    content = {
        'form' : form
    }
    return render_template('login.html', **content)

@authentication.route('logout')
def logout():
    logout_user()
    flash("You have successfully logged out!", 'info')
    return redirect(url_for('authentication.login'))

