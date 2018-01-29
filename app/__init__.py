from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)


    # will add views from forms
    return app