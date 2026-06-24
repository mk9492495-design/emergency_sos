from flask import Blueprint, render_template
from db import get_connection

history_bp = Blueprint('history', __name__)

@history_bp.route('/history')
def history():

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT *
            FROM sos_alerts
            ORDER BY alert_id DESC
        """)

        alerts = cursor.fetchall()

    except:
        alerts = []

    cursor.close()
    conn.close()

    return render_template(
        'history.html',
        alerts=alerts
    )