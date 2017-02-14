# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
rhizopathy - test_model_root.py
Created on 2/13/17.


"""
# Stdlib
import logging
import os
# Third party code
import pytest
# Custom code
from rhizopathy.constants import root as rc
from rhizopathy.models import root

# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)

# Assets Configuration
ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
assert os.path.isdir(ASSETS)


@pytest.fixture()
def attr_map():
    _map = {'foo': 'bar',
            'duck': 'quack',
            }
    return _map


@pytest.fixture()
def root_args():
    rn = 'R1'
    loc = 1
    bs = 1
    return rn, loc, bs


@pytest.fixture()
def root_obj(attr_map, root_args):
    rn, loc, bs = root_args
    obj = root.Root(attr_map=attr_map,
                    rootname=rn,
                    location=1,
                    birthsession=1
                    )
    return obj


class TestRootIdentity:
    def test_identity_tuple(self):
        r1 = root.RootIdentity('foo', 'bar', 'duck')
        assert len(r1) == 3
        assert r1.get(rc.ROOT_NAME) == 'foo'
        assert r1.get(rc.LOCATION) == 'bar'
        assert r1.get(rc.BIRTH_SESSSION) == 'duck'
        # These tests are fragile if we change column values ever
        assert r1.rootname == 'foo'
        assert r1.location == 'bar'
        assert r1.birthsession == 'duck'

    def test_equivalence(self):
        # Positive
        r1 = root.RootIdentity('foo', 'bar', 'duck')
        rt = root.RootIdentity('foo', 'bar', 'duck')
        assert r1 == rt
        # Negative
        rt = root.RootIdentity('foo', 'bar', 'quack')
        assert r1 != rt
        rt = root.RootIdentity('foo', 'dog', 'duck')
        assert r1 != rt
        rt = root.RootIdentity('nano', 'bar', 'duck')
        assert r1 != rt


class TestModelRoot:

    def test_model_root(self, root_obj, root_args):
        rn, loc, bs = root_args
        ri = root.RootIdentity(rn, loc, bs)

        assert root_obj.identity == ri
        assert root_obj.anomaly == ''
        assert root_obj.isAlive == ''
        assert root_obj.censored == ''
        assert root_obj.highestOrder == ''

    def test_root_set(self, root_obj, caplog):

        root_obj.set('foo', 'paper')
        assert root_obj.bar == 'paper'

        root_obj.set('paper', 'A4')
        assert 'Cannot set key:' in caplog.text

        r = root_obj.get('foo')
        assert r == 'paper'

        r = root_obj.get('duck')
        assert 'Cannot retrieve key' not in caplog.text
        assert r is None

        r = root_obj.get('paper')
        assert r is None
        assert 'Cannot retrieve key' in caplog.text

        r = root_obj.get('paper', 'defaulty')
        assert r == 'defaulty'

