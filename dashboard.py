from flask import Blueprint, render_template, session, redirect
from db import get_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user' not in session:
        return redirect('/login')

    # Optional: Database se dynamic data fetch karne ke liye try-except block
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        # Yahan aap apna query likh sakte hain jo dashboard.html par bhejna ho
        # cursor.execute("SELECT * FROM ...")
        
        cursor.close()
        connection.close()
    except Exception as e:
        print("Database error:", e)

    return render_template('dashboard.html')
