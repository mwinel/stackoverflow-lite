from flask import Flask
from app.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    # Register blueprints
    from app.main.index import blueprint as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/api/v1')

    from app.main.questions import blueprint as questions_blueprint
    app.register_blueprint(questions_blueprint, url_prefix='/api/v1')

    from app.main.answers import blueprint as answers_blueprint
    app.register_blueprint(answers_blueprint, url_prefix='/api/v1')

    return app
