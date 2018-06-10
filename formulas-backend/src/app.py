#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
from eve import Eve
from flask import jsonify
import json

mongo_host = os.environ.get('MONGO_HOST')
service_port = 8087

eve_settings = {}
eve_settings['MONGO_HOST'] = mongo_host
eve_settings['MONGO_DBNAME'] = 'formulas'
eve_settings['DEBUG'] = True

eve_settings['SOFT_DELETE'] = True
eve_settings['API_VERSION'] = 'v1'
eve_settings['VERSIONING'] = False
eve_settings['RENDERERS'] = ['eve.render.JSONRenderer']
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=service_port)
