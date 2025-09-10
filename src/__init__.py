from flask import Flask
from src.config import get_config


def create_app(config_name='development'):
    """Application factory pattern for creating Flask app instances."""
    app = Flask(__name__)
    
    # Load configuration based on environment
    app.config.from_object(get_config(config_name))
    
    # Register blueprints
    from src.blueprints import register_blueprints
    register_blueprints(app)
    
    return app