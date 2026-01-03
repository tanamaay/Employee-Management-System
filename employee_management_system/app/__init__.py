from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register Blueprints
    from .controller.employee_controller import employee_bp
    app.register_blueprint(employee_bp, url_prefix='/employees')

    # Create DB tables
    with app.app_context():
        db.create_all()

    return app
