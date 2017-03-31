#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Provides Event Hooks against REST Resources.

This module is the mastermind controlling the
flow of triggers and events to resources
"""

import traceback
from settings import (LANGUAGES,
                      LANGUAGE_DEFAULT,
                      XTRAPOP)

__author__ = "Sanjay Joshi"
__copyright__ = "IBM Copyright 2016"
__credits__ = ["Sanjay Joshi"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__maintainer__ = "Sanjay Joshi"
__email__ = "joshisa@us.ibm.com"
__status__ = "Prototype"


# Pre-Request Event Hook example
def before_returning_items(resource, request, lookup):
    try:
        desiredLang = request.accept_languages.best_match(LANGUAGES.keys(),
                                                          LANGUAGE_DEFAULT)
        print("The best matched Accept-Language Header is: " + desiredLang +
              " (" + LANGUAGES.get(desiredLang) + ")")
    except Exception as e:
        print(e)
        traceback.print_exc()


def on_fetched_resource_firstone(response):
    try:
        print("Returning first response element only")
        # Stash first entry
        if len(response['_items']) > 0:
            newresponse = response['_items'][0]
        else:
            newresponse = {}
        # Trash entire item array
        del(response['_items'])
        # Add stashed entry
        response.update(newresponse)
        # OPTIONAL: Pop off extra fields
        if XTRAPOP:
            response.pop('cloudhost', None)
            response.pop('_updated', None)
            response.pop('_id', None)
            response.pop('_created', None)
            response.pop('_etag', None)
    except Exception as e:
        print(e)
        traceback.print_exc()


def on_fetched_resource_xtrapop(response):
    try:
        print("Returning xtrapop formatted response")
        if len(response['_items']) > 0 and XTRAPOP:
            for webster in response['_items']:
                webster.pop('cloudhost', None)
                webster.pop('_updated', None)
                webster.pop('_id', None)
                webster.pop('_created', None)
                webster.pop('_etag', None)
        myresponse = response['_items']
        # Trash entire item array
        del(response['_items'])
        # Add stashed entry
        response['types'] = myresponse

    except Exception as e:
        print(e)
        traceback.print_exc()


# Post-Request Event Hook example
def after_returning_items(resource, request):
    try:
        print('A GET on the "%s" endpoint was just performed!' % resource)
    except Exception as e:
        print(e)
        traceback.print_exc()
