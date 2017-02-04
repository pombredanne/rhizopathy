# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
rhizopathy - data_ingestion.py
Created on 2/3/17.


"""
# Stdlib
import json
import logging
import os
import sys
# Third party code
import pytest

# Custom code
from rhizopathy import utils
from rhizopathy.constants import workbook

# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)

# Assets Configuration
ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
assert os.path.isdir(ASSETS)

log.info(ASSETS)

def get_file(fn):
    fp = os.path.join(ASSETS, fn)
    log.info('asset contents:{}'.format(os.listdir(ASSETS)))
    log.info(fp)
    assert os.path.isfile(fp)
    return fp


class TestDataIngestion:

    def test_simple_text_ingestion(self, caplog):
        fn = 'MSS_Analysis_Tube 1_Updated.TXT'
        fp = get_file(fn)
        assert fn in caplog.text
        r = utils.ingest_text.ingest(fp=fp)
        assert len(r) == 527

    def test_workbook_constants(self, caplog):
        keys = [getattr(workbook, name) for name in dir(workbook) if name.startswith('COLUMN_')]
        assert len(keys) > 4  # XXX Kind of a arbitrary number.
        fn = 'MSS_Analysis_Tube 1_Updated.TXT'
        fp = get_file(fn)

        r = utils.ingest_text.ingest(fp=fp)
        for row in r:
            for key in keys:
                assert key in row
