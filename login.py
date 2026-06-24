from flask import Blueprint, render_template, request, session, redirect

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if email:
            session['user'] = email   # IMPORTANT FIX
            return redirect('/dashboard')

    return render_template('login.html')