# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
rhizopathy - workbook.py
Created on 2/3/17.

Constants related to working with text or xlsx workbook data.
"""
import logging

log = logging.getLogger(__name__)

# TXT Header data
ROOT_HEADER_KEY = 'ROOT'

# Workbook data
ROOT_WORKBOOK_TAB_NAME = 'ROOT'

# Column names
COLUMN_ROOTNAME = 'RootName'
COLUMN_EXPERIMENT = 'Experiment'
COLUMN_TUBE_NUMBER = 'Tube#'
COLUMN_LOCATION_NUMBER = 'Location#'
COLUMN_DATE = 'Date'
COLUMN_TIME = 'Time'
COLUMN_SESSION_NUMBER = 'Session#'
COLUMN_GATAHER = 'DataGatherer'
COLUMN_BIRTHSESSION = 'BirthSession'
COLUMN_DEATHSESSION = 'DeathSession'
COLUMN_ORDER = 'Order'
COLUMN_TIPLIVSTATUS = 'TipLivStatus'
COLUMN_ROOTNOTES = 'RootNotes'
COLUMN_HIGHESTORDER = 'HighestOrder'
# COLUMN_MYCO = 'Myco'  # XXX This is not present in the MSS Dataset ???
COLUMN_TIP_DIAMETER = 'TipDiam'

