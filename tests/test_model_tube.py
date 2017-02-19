# -*- coding: utf-8 -*-
"""
rhizopathy - test_model_tube.py
Created on 2/19/17.

Tests for the Tube model
"""
# Stdlib
import json
import logging
import os
import sys

# Third party code
import pytest

# Custom code
from rhizopathy.exc import TubeError
from rhizopathy.models import root
from rhizopathy.models import tube


# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)

# Assets Configuration
ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
assert os.path.isdir(ASSETS)


class TestTube:  # XXX CamelCase

    def test_tube_simple(self):
        tn = 1
        t = tube.Tube(tubenumber=tn)
        assert t.tubeNumber == tn
        assert t.roots == []

    def test_magic_methods(self):
        tn = 1
        t = tube.Tube(tubenumber=tn)
        assert len(t) == 0
        # This is a direct object access - just testing the magic methods though.
        t.roots.append(1)
        t.roots.append(2)
        t.roots.append(3)
        assert len(t) == 3
        e = [1, 2, 3]
        l = [root for root in t]
        assert l == e

    def test_root_insertion_bad(self):
        t = tube.Tube(tubenumber=1)
        with pytest.raises(TubeError) as cm:
            t.insert_or_update_root(root={'key': 1})
        assert 'Invalid type provided: ' in str(cm.value)

    def test_root_insertion(self, caplog):
        t = tube.Tube(tubenumber=1)
        # XXX This feels like shitty code.
        # This is really what the Fields object mapper is supposed to do FOR me.
        am = {'Tube#': 'TubeX',
              'Session#': 'SessionX'}
        for i in range(1, 3):
            for j in range(1, 3):
                for k in range(1, 3):
                    rn = 'R{}'.format(i)
                    r = root.Root(attr_map=am,
                                  rootname=rn,
                                  location=j,
                                  birthsession=k)
                    t.insert_or_update_root(root=r)
        assert 'Adding root to tube' in caplog.text
        assert len(t) == 8
