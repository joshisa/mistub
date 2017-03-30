#!/usr/bin/env python
"""Contains the Unit Tests for the REST Resources.

Contains the Unit Tests for exercising all provided
API Endpoints for the Python Eve REST Server
"""

import requests

__author__ = "Sanjay Joshi"
__copyright__ = "Copyright 2016 IBM"
__credits__ = ["Sanjay Joshi"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sanjay Joshi"
__email__ = "joshisa@us.ibm.com"
__status__ = "Demo"


ROOT_TEST_URL = 'http://localhost:5005'
DOC_PATH = '/docs'


def test_base_eve_docs_no_content_type_response():
    """ Read Base EVE DOCS URL without Content Type"""
    url = ''.join([ROOT_TEST_URL, DOC_PATH])
    headers = {}
    r = requests.get(url, headers=headers)
    assert r.status_code == requests.codes.ok  # 200
