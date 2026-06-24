from flask import Flask

from login import login_bp
from register import register_bp
from dashboard import dashboard_bp
from contacts import contacts_bp
from profile import profile_bp
from history import history_bp
from sos import sos_bp

app = Flask(__name__)
app.secret_key = "emergency_sos_key"

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(history_bp)
app.register_blueprint(sos_bp)

if __name__ == "__main__":
    app.run(debug=True)