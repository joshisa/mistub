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
    'url': 'corpora/ada_diabetes',
    'schema': {
        'cloudhost': {
            'type': 'string',
            'default': 'Powered by IBM Bluemix and Python Eve'
        },
        'corpusName': {
            'type': 'string',
            'default': 'library_of_congress'
        },
        'descriptiveName': {
            'type': 'string',
            'default': 'Doh!MissingDescription'
        },
        'pathParams': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'default': 'Doh!Missingparams'
            }
        },
        'latest': {
            'type': 'boolean',
            'default': False
        },
        'corpusVersion': {
            'type': 'string',
            'default': 'v1'
        },
        'umlsVersion': {
            'type': 'string',
            'default': 'Doh!MissingumlsVersion'
        },
        'umlsRelease': {
            'type': 'string',
            'default': 'Doh!MissingumlsRelease'
        },
        'access': {
            'type': 'string',
            'default': 'Doh!MissingAccess'
        },
        'defaultCorpus': {
            'type': 'boolean',
            'default': False
        }
    },
    'allow_unknown': True
}
