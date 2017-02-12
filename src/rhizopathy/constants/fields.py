# -*- coding: utf-8 -*-
"""
rhizopathy - fields.py
Created on 2/8/17.

Constants related to fields models.
"""

# strings related to root birth and final stages.
ROOT_BIRTH = 'BIRTH'
ROOT_FINAL = 'FINAL'

# Validation strings for identifying good/bad attrs via regex.
NUM = r'0-9'
ALPHA = r'a-zA-Z'
ALPHA_UNDER = r'{alpha}_'.format(alpha=ALPHA)
ALPHA_NUM_UNDER = r'{alpha_under}{num}'.format(alpha_under=ALPHA_UNDER, num=NUM)
ALPHA_NUM_UNDER_CLASS = r'[{alpha_num_under}]'.format(alpha_num_under=ALPHA_NUM_UNDER)
DIGIT_START = r'^[{num}]'.format(num=NUM)
VALID_PYTHON_IDENTIFIER = r'^[{alpha_under}]+[{alpha_num_under}]*$'.format(alpha_under=ALPHA_UNDER,
                                                                           alpha_num_under=ALPHA_NUM_UNDER)
INVALID_PYTHON_IDENTIFIERS = r'[^{alpha_num_under}]'.format(alpha_num_under=ALPHA_NUM_UNDER)
REPLACEMENT_STR = 'X'
