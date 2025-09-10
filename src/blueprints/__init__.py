from src.routes import user_blueprint


def register_blueprints(app):
    """Register all blueprints with the Flask application."""
    app.register_blueprint(user_blueprint, url_prefix='/api')