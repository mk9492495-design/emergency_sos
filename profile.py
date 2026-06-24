from flask import Blueprint, render_template, session, redirect

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def profile():

    if 'user' not in session:
        return redirect('/login')

    return render_template('profile.html', user=session['user'])