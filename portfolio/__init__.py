
#!/usr/bin/python3
"""init file for the app"""

from flask import Flask
from config import DevelopmentConfig



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Register Blueprints
from portfolio.birthday import birthday_bp
app.register_blueprint(birthday_bp)
from portfolio.admin import admin_bp
app.register_blueprint(admin_bp)

from portfolio.database import session
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)