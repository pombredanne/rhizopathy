# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
rhizopathy - root.py
Created on 2/8/17.

Class for representing and storing data about roots.
"""
# Stdlib
import collections
import logging
# Third Party Code
# Custom Code
from rhizopathy.constants.root import ROOT_NAME
from rhizopathy.constants.root import LOCATION
from rhizopathy.constants.root import BIRTH_SESSSION
from rhizopathy.constants.root import IS_ALIVE
from rhizopathy.constants.root import CENSORED
from rhizopathy.constants.root import HIGHEST_ORDER
from rhizopathy.constants.root import ANOMALY
from rhizopathy.constants.root import ROOT_IDENTITY

log = logging.getLogger(__name__)
__author__ = 'wgibb'


# Named tuples allow for the analyzer to create values for uniquely identifying roots if needed.
class RootIdentity(collections.namedtuple(ROOT_IDENTITY,
                                          [ROOT_NAME, LOCATION, BIRTH_SESSSION])):
    __slots__ = ()

    def get(self, value):
        return getattr(self, value)


# The following docstring defitinos only works in Python 3.5 in testing :(
# RootIdentity.__doc__ = 'Store information used to uniquely identify a root in a tube.'
# getattr(RootIdentity, ROOT_NAME).__doc__ = 'Name of the root'
# getattr(RootIdentity, LOCATION).__doc__ = 'Location of the root in a tube.'
# getattr(RootIdentity, BIRTH_SESSSION).__doc__ = 'Session when the root was first observed.'


class Root(object):
    fixed_attributes = [IS_ALIVE, CENSORED, HIGHEST_ORDER, ANOMALY]

    def __init__(self, attr_map, rootname, location, birthsession):
        self.attr_map = attr_map
        self.identity = RootIdentity(rootname=rootname,
                                     location=location,
                                     birthsession=birthsession)
        self.anomaly = ''
        self.isAlive = ''
        self.censored = ''
        self.highestOrder = ''

    def set(self, key, value):
        new_key = self.attr_map.get(key, None)
        if not new_key:
            log.warning('Cannot set key: {}'.format(key))
            return
        setattr(self, new_key, value)

    def get(self, key, default=None):
        new_key = self.attr_map.get(key)
        if not isinstance(new_key, str):
            log.warning('Cannot retrieve key: {}'.format(key))
            return default
        return getattr(self, new_key, default)
