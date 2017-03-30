#!/usr/bin/env python
"""Contains the Data Model for a cool Resource.

"""
__author__ = "Sanjay Joshi"
__copyright__ = "IBM Copyright 2017"
__credits__ = ["Sanjay Joshi"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sanjay Joshi"
__email__ = "joshisa@us.ibm.com"
__status__ = "Prototype"

schema = {
    'url': 'status',
    'schema': {
        'cloudhost': {
            'type': 'string',
            'default': 'Powered by IBM Bluemix and Python Eve'
        },
        'version': {
            'type': 'string',
            'default': '1.0.0 2017-03-28T02:15:49Z'
        },
        'upTime': {
            'type': 'string',
            'default': '1d 18:35:00'
        },
        'serviceState': {
            'type': 'string',
            'default': 'OK'
        },
        'stateDetails': {
            'type': 'string',
        },
        'hostName': {
            'type': 'string',
            'default': 'foo.watson.bar'
        },
        'requestCount': {
            'type': 'integer',
            'default': 0
        },
        'maxMemoryMb': {
            'type': 'integer',
            'default': 0
        },
        'commitedMemoryMb': {
            'type': 'integer',
            'default': 0
        },
        'inUseMemoryMb': {
            'type': 'integer',
            'default': 0
        },
        'availableProcessors': {
            'type': 'integer',
            'default': 0
        },
    },
    'allow_unknown': True
}
