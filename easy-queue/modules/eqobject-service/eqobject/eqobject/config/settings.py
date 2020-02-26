import os
# Application
APP_CONTEXT_PATH = "/eqobject/api"
# Flask settings
FLASK_SERVER_NAME = 'localhost:15000'
FLASK_DEBUG = True  # Do not use debug mode in production

# Log settings 
LOG_FILE_BASE = 'easyqueue-eqobject'
LOG_FOLDER = r"./eqobject/eqobject/logs/"
LOG_FORMAT = "[%(asctime)s]  %(levelname)s  %(name)s.%(funcName)s:%(lineno)d - %(message)s"

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# Database settings
MONGODB_URI = os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else 'mongodb://localhost:27017/'
MONGODB_DATABASE = 'easy_queue'
MONGODB_COLLECTION = 'eqobject'

# Gateway settings
GATEWAY_URI = os.environ['GATEWAY_URI'] if 'GATEWAY_URI' in os.environ else 'http://localhost:15100/'
