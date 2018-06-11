#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
from eve import Eve
from flask import jsonify
import json
from eve_swagger import swagger, add_documentation

mongo_host = os.environ.get('MONGO_HOST')
service_port = 8087

eve_settings = {}
eve_settings['MONGO_HOST'] = mongo_host
eve_settings['MONGO_DBNAME'] = 'formulas'
eve_settings['DEBUG'] = True

eve_settings['SWAGGER_INFO'] = {
    'title': 'TexLive backend service',
    'version': '1.0',
    'description': '',
    'termsOfService': '',
    'contact': {
        'name': 'WikiTolearn.org',
        'url': 'mailto:sysadmins@wikitolearn.org'
    },
    'license': {
        'name': 'AGPLv3+',
        'url': 'https://www.gnu.org/licenses/agpl-3.0.html',
    },
    'schemes': ['http', 'https'],
}

eve_settings['SOFT_DELETE'] = True
eve_settings['API_VERSION'] = 'v1'
eve_settings['VERSIONING'] = False
eve_settings['RENDERERS'] = ['eve.render.JSONRenderer']
# It raise a warning but it needs to generate a valid Swagger doc
eve_settings['XML'] = False
eve_settings['RESOURCE_METHODS'] = ['GET', 'POST']
eve_settings['ITEM_METHODS'] = ['GET', 'PATCH', 'DELETE']
eve_settings['EXTENDED_MEDIA_INFO'] = ['content_type', 'name', 'length']
eve_settings['RETURN_MEDIA_AS_BASE64_STRING'] = False
eve_settings['RETURN_MEDIA_AS_URL'] = True
eve_settings['MEDIA_ENDPOINT'] = 'rendered-formulas'
eve_settings['DOMAIN'] = {}
eve_settings['DOMAIN']['formulas'] = {
    'schema': {
        'formula': {
            'type': 'string',
            'required': True
        },
        'svg': {
            'type': 'media',
            'required': True
        },
    },
}


app = Eve(settings=eve_settings)
app.register_blueprint(swagger)

# Update Swagger doc
add_documentation({
  'paths': {
    '/rendered-formulas/{renderedFormulaId}': {
      'get': {
        'parameters': [{
          'in': 'path',
          'name': 'renderedFormulaId',
          'required': True,
          'description': 'The id of the svg media',
          'type': 'string',
        }],
        'responses': {
          '200': {
            'description': 'Formula svg fetched successfully',
            'type': 'media',

          }
        }
}}}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=service_port)
