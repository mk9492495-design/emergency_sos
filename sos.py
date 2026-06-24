from flask import Blueprint, render_template, request, session
from db import get_connection

sos_bp = Blueprint('sos', __name__)

@sos_bp.route('/sos', methods=['GET', 'POST'])
def sos():

    message = ""

    if request.method == 'POST':

        conn = get_connection()
        cursor = conn.cursor()

        user_id = session.get('user')  # login user

        if not user_id:
            return "User not logged in"

        cursor.execute("""
            INSERT INTO sos_alerts
            (user_id, location, status)
            VALUES (%s, %s, %s)
        """, (
            user_id,
            "Location Not Available Yet",
            "SOS Sent"
        ))

        conn.commit()

        cursor.close()
        conn.close()

        message = "🚨 SOS Alert Sent Successfully"

    return render_template('sos.html', message=message)