from flask import Flask
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from config import Config
from .extensions import db



def create_app(config_class=Config):
    app = Flask(__name__)
    csrf = CSRFProtect()

    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)
    Migrate(app, db)

    # Set the Content Security Policy
    Talisman(
        app,
        content_security_policy={
            'default-src': "'self'",
            'style-src': "'self' 'unsafe-inline'",
            'script-src': "'self' 'unsafe-inline' 'unsafe-eval'",
        }
    )

    register_blueprints(app)

    return app


def register_blueprints(app):
    from core.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')
