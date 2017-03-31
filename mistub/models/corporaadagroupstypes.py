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
    'url': 'corpora/ada_diabetes/groups/all/types',
    'schema': {
        'cloudhost': {
            'type': 'string',
            'default': 'Powered by IBM Bluemix and Python Eve'
        },
        'type': {
            'type': 'string',
            'default': 'Doh!MissingType'
        },
        'parent': {
            'type': 'string',
            'default': 'Doh!MissingParent'
        },
        'group': {
            'type': 'string',
            'default': 'Doh!MissingGroup'
        },
        'children': {
            'type': 'list',
            'schema': {
                'type': 'dict'
            }
        }
    },
    'allow_unknown': True
}
