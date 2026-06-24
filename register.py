from flask import Blueprint, render_template, request, redirect

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            return "Passwords do not match"

        print("New User Registration")
        print("Name:", full_name)
        print("Email:", email)
        print("Phone:", phone)

        return redirect('/login')

    return render_template('register.html')