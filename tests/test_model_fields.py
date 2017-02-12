# -*- coding: utf-8 -*-
"""
rhizopathy - test_model_fields.py
Created on 2/8/17.

Tests for rhizopath.models.fields
"""
# Stdlib
import argparse
import json
import logging
import os
import re
import sys

# Third Party Code
import pytest

from rhizopathy.constants import fields as fc
from rhizopathy.exc import FieldsError
from rhizopathy.models import fields

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def validator():
    obj = fields.AttrValidator()
    return obj


class TestAttrValidator:

    def test_classmethod(self):
        k = 'value'
        assert fields.AttrValidator.scrub_attr(k) == k

    def test_scrub_callable(self, validator):
        bad_values = ['scrub_attr', '__repr__']
        for k in bad_values:
            with pytest.raises(FieldsError) as cm:
                r = validator.scrub_attr(value=k)
                assert r is None
            assert 'Cannot create a field for a callable name.' in str(cm.value)


    def test_scrub_1(self, validator):
        values = [('foobar', 'foobar'),
                  ('foo bar', 'foo{r}bar'.format(r=fc.REPLACEMENT_STR)),
                  ('_foobar', '_foobar'),
                  ('1234', '{r}1234'.format(r=fc.REPLACEMENT_STR)),
                  ('fo^o%ba*r', 'fo{r}o{r}ba{r}r'.format(r=fc.REPLACEMENT_STR)),
                  ]
        for k, e in values:
            assert validator.scrub_attr(value=k) == e

    def test_scrub_fail(self, validator):
        bad_values = ['', '*', '&#$']
        for k in bad_values:
            with pytest.raises(FieldsError) as cm:
                r = validator.scrub_attr(value=k)
                assert r is None
            assert 'Key contains no valid python identifiers' in str(cm.value)

    def test_whitelist(self, validator):
        with pytest.raises(FieldsError) as cm:
            validator.scrub_attr(value='foobar', whitelist=['foobar'])
        assert 'Key value is whitelisted' in str(cm.value)


class TestIdentityFields:

    def test_basic_class(self):
        assert len(fields.IdentityFields.identity_attributes) == 4
        assert len(fields.IdentityFields.identity_fields) == 4

    def test_mapping(self):
        found_default_mapping = False
        for k, v in fields.IdentityFields.identity_attributes.items():
            if re.search(fc.VALID_PYTHON_IDENTIFIER, k):
                continue
            assert fc.REPLACEMENT_STR in v
            found_default_mapping = True
        assert found_default_mapping is True


class TestRootDataFields:

    def test_basic_class(self):
        obj = fields.RootDataFields()
        assert len(obj.required_attributes) == 10

    def test_additional_fields(self):
        additional_fields = {'foobar': fc.ROOT_BIRTH,
                             'myco': fc.ROOT_FINAL,
                             }
        obj = fields.RootDataFields(additional_fields=additional_fields)
        assert len(obj.required_attributes) == 12
        assert len(obj.custom_attributes) == 2

    def test_additional_fields_bad1(self):
        additional_fields = {'foobar': fc.ROOT_BIRTH,
                             'myco': 'oh snap',
                             }
        with pytest.raises(FieldsError) as cm:
            obj = fields.RootDataFields(additional_fields=additional_fields)
        assert 'Unknown custom field propogation value' in str(cm.value)

    def test_additional_fields_bad2(self):
        additional_fields = {'Session#': fc.ROOT_BIRTH,
                             }
        with pytest.raises(FieldsError) as cm:
            obj = fields.RootDataFields(additional_fields=additional_fields)
        assert 'Additional field duplicates a required field' in str(cm.value)

    def test_additional_fields_bad3(self):
        additional_fields = {'*': fc.ROOT_BIRTH,
                             }
        with pytest.raises(FieldsError) as cm:
            obj = fields.RootDataFields(additional_fields=additional_fields)
        assert 'Key contains no valid python identifiers' in str(cm.value)
