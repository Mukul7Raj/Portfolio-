from flask import Flask
from flask_mail import Mail
import os

mail = Mail()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object('config.Config')
    
    # Initialize extensions
    mail.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Ensure static and templates folders exist
    os.makedirs(os.path.join(app.root_path, 'static'), exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'templates'), exist_ok=True)
    os.makedirs(os.path.join(app.root_path, 'static/images'), exist_ok=True)
    
    return app 