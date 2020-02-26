import os
import platform
import logging
import logging.config
from datetime import datetime

from flask.logging import default_handler
from flask import Flask, Blueprint

from eqobject.config import settings
from eqobject.api.eqobject.endpoints.eqobject import ns as eqobject_namespace
from eqobject.api.restplus import api
from eqobject.api.status.endpoints.status import ns as status_namespace
from eqobject.database import db

app = Flask(__name__)
log = app.logger

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['MONGODB_URI'] = settings.MONGODB_URI
    flask_app.config['MONGODB_DATABASE'] = settings.MONGODB_DATABASE
    flask_app.config['MONGODB_COLLECTION'] = settings.MONGODB_COLLECTION
    flask_app.config['GATEWAY_URI'] = settings.GATEWAY_URI
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def configure_log(flask_app):
    
    log_file = '{}-{:%Y-%m-%d}.log'.format(settings.LOG_FILE_BASE, datetime.utcnow()) 
    app.logger.removeHandler(default_handler)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    gunicorn_logger.setLevel(logging.INFO)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    
    log_file_path = settings.LOG_FOLDER
    if not os.path.exists(settings.LOG_FOLDER):
        if (platform.system() == "Windows"):
            log_file_path = "~/"
        else:
            log_file_path = "/var/log"

    file_handler = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(log_file_path, log_file), when='midnight', backupCount=10)
    file_handler.setFormatter(logging.Formatter(settings.LOG_FILE_BASE + " " + settings.LOG_FORMAT))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

def initialize_app():
    configure_app(app)
    configure_log(app)
    blueprint = Blueprint('api', __name__, url_prefix=settings.APP_CONTEXT_PATH)
    api.init_app(blueprint)
    api.add_namespace(eqobject_namespace)
    api.add_namespace(status_namespace)
    app.register_blueprint(blueprint)

    return app

