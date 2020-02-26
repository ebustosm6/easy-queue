import logging

from http import HTTPStatus
from flask import request
from flask_restplus import Resource
from eqobject.api.eqobject.business import (
    request_eq_object, request_eq_objects, create_eq_object, create_eq_objects, update_eq_object, delete_eq_object
    )
from eqobject.api.eqobject.serializers import eq_object
from eqobject.api.restplus import api
from easyqueue.core.base import EQObject, schema_eqobject

log = logging.getLogger(__name__)

ns = api.namespace('eqobject', description='Operations related to EQ base Objects')

@ns.route('/')
class EQObjectCollection(Resource):

    @api.marshal_with(eq_object, as_list=True)
    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def get(self):
        """
        Returns list of EQ Objects.
        """
        
        return request_eq_objects(), 200

    @api.expect([eq_object])
    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def post(self):
        """
        Creates several EQ Object.
        """
        data = request.json
        return create_eq_objects(data), 200


@ns.route('/<id>')
class EQObjectItem(Resource):

    @api.marshal_with(eq_object)
    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def get(self, id):
        """
        Returns a EQ Object.
        """
        print("Get one EQObject: {}".format(id))
        return request_eq_object(id), 200

    @api.expect(eq_object)
    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def post(self, id):
        """
        Creates a EQ Object.
        """
        data = request.json
        data["_id"] = id
        return create_eq_object(data), 200

    @api.expect(eq_object)
    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def put(self, id):
        """
        Updates a EQ Object.
        """
        data = request.json
        return update_eq_object(id, data), 200

    @api.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unexpected server error.')
    def delete(self, id):
        """
        Deletes EQ Object.
        """
        return delete_eq_object(id), 200

