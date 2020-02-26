import eqobject.config.settings as settings
from eqobject.setup.app import initialize_app, log

app = initialize_app()

if __name__ == '__main__':
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)
