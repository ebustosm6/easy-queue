import logging

from http import HTTPStatus
from flask import request
from flask_restplus import Resource

from eqobject.api.restplus import api
from easyqueue.core.base import EQObject, schema_eqobject

log = logging.getLogger(__name__)

ns = api.namespace('status', description='Health check')

@ns.route('/health')
class StatusEndpoint(Resource):

    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def get(self):
        """
        Returns OK
        """
        return dict(status="OK"), HTTPStatus.OK

