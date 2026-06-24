import os
from flask import Flask, render_template, redirect

# Blueprints import
from login import login_bp
from register import register_bp
from dashboard import dashboard_bp
from contacts import contacts_bp
from profile import profile_bp
from history import history_bp
from sos import sos_bp

app = Flask(__name__)
app.secret_key = "emergency_sos_key"

# Default root route - Website khulte hi login page par bhej dega
@app.route("/")
def home():
    return redirect('/login')

# Blueprints Register karna
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(history_bp)
app.register_blueprint(sos_bp)

if __name__ == "__main__":
    # Render ke liye dynamic port configuration (Render port 10000 deta hai)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
