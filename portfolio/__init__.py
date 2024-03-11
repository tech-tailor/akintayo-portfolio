
#!/usr/bin/python3
"""init file for the app"""

from flask import Flask
from config import DevelopmentConfig



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
print('SECRET_KEY: ', app.config['DEBUG'])
 





# Register Blueprints
from portfolio.birthday import birthday_bp
app.register_blueprint(birthday_bp)


print('SECRET_KEY2: ', app.config['SECRET_KEY'])
# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)