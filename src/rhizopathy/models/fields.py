# -*- coding: utf-8 -*-
"""
rhizopathy - fields.py
Created on 2/8/17.

Stores the Synthesis and ROOT tab fields that we care about.
"""
# Stdlib
import logging
import re
# Third Party Code
# Custom Code
from rhizopathy.constants.fields import ROOT_BIRTH, ROOT_FINAL, VALID_PYTHON_IDENTIFIER, INVALID_PYTHON_IDENTIFIERS, \
    REPLACEMENT_STR, DIGIT_START, ALPHA_NUM_UNDER_CLASS
from rhizopathy.exc import FieldsError

log = logging.getLogger(__name__)



class AttrValidator(object):

    @classmethod
    def scrub_attr(cls, value, whitelist=None):
        if not whitelist:
            whitelist = []
        new_key = str(value)
        if new_key in whitelist:
            raise FieldsError('Key value is whitelisted.')
        if not re.search(ALPHA_NUM_UNDER_CLASS, new_key):
            raise FieldsError('Key contains no valid python identifiers.')
        if not re.search(VALID_PYTHON_IDENTIFIER, new_key):
            new_key = re.sub(INVALID_PYTHON_IDENTIFIERS, REPLACEMENT_STR, new_key)
            if re.search(DIGIT_START, new_key):
                new_key = ''.join([REPLACEMENT_STR, new_key])
            if not re.search(VALID_PYTHON_IDENTIFIER, new_key):
                raise FieldsError('Unable to scrub value into a valid python identifier [{}]'.format(value))
        if hasattr(cls, new_key) and callable(getattr(cls, new_key)):
            raise FieldsError('Cannot create a field for a callable name.')
        return new_key


class IdentityFields(AttrValidator):
    identity_fields = ['RootName',
                       'Location#',
                       'BirthSession',
                       'Tube#']

    identity_attributes = {}
    for k in identity_fields:
        new_key = AttrValidator.scrub_attr(value=k)
        identity_attributes[k] = new_key


class RootDataFields(IdentityFields):
    def __init__(self, additional_fields=None):
        self.base_fields = ['Session#',
                            'DeathSession',
                            'TipLivStatus',
                            'NumberOfTips',
                            'Date',
                            'Order']

        self.required_attributes = {k: v for k, v in IdentityFields.identity_attributes.items()}

        for k in self.base_fields:
            new_key = self.scrub_attr(value=k)
            self.required_attributes[k] = new_key

        self.additional_fields = {}
        self.custom_attributes = {}

        if additional_fields:
            self.additional_fields = additional_fields
            for k, v in self.additional_fields.items():
                log.info('Preparing to extract custom field [{}]'.format(k))
                if k in self.required_attributes:
                    raise FieldsError('Additional field duplicates a required field [{}]'.format(k))
                if v not in [ROOT_BIRTH, ROOT_FINAL]:
                    raise FieldsError('Unknown custom field propogation value [{}][{}]'.format(k, v))
                new_key = self.scrub_attr(value=k)
                self.custom_attributes[k] = new_key
                self.required_attributes[k] = new_key


# Commented out until addressing data synthesis problem
# class SynthesisDataFields(IdentityFields):
#     def __init__(self):
#         self.synthesis_fields = ['AliveTipsAtBirth',
#                                  'AliveTipsAtDeath', ]
#         self.required_attributes = {k: v for k, v in IdentityFields.identity_attributes.items()}
#
#         for k in self.synthesis_fields:
#             new_key = str(k)
#             if not re.search(valid_python_identifer, new_key):
#                 new_key = re.sub(invalid_python_identifiers, replacement_str, new_key)
#                 if re.search(digit_start, new_key):
#                     new_key = ''.join([replacement_str, new_key])
#                 if not re.search(valid_python_identifer, new_key):
#                     raise FieldsError('Unable to scrub synthesis field into a valid python identifier [{}]'.format(k))
#             self.required_attributes[k] = new_key
