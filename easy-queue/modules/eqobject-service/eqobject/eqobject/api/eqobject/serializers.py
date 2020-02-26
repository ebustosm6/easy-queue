from flask_restplus import fields
from eqobject.api.restplus import api

eq_object = api.model('EQ object', {
    '_id': fields.String(readOnly=True, description='The unique identifier of a EQ Object'),
    '_created_at': fields.String(required=True, description='Created date in ISO format'),
    '__type__': fields.String(required=True, description='EQ Object type')
    
})
