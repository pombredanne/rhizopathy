#!/usr/bin/env python
# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
rhizopathy - ingest_text.py
Created on 2/3/17.


"""
# StdLib
import argparse
import json
import logging
import sys
# Third Party Code
# Custom code
from rhizopathy.constants import workbook

log = logging.getLogger(__name__)


def ingest(fp):
    """

    :param fp:
    :return:
    """

    with open(fp, 'rb') as f:
        lines = f.readlines()
    lines = [line.decode().strip().split('\t') for line in lines]

    headers = lines[0:4]
    try:
        root_header = [h for h in headers if workbook.ROOT_HEADER_KEY in h][0]
    except IndexError:
        log.error('Unable to find ROOT header')
        raise
    root_index = root_header.index(workbook.ROOT_HEADER_KEY)
    root_rows = [line for line in lines[4:] if line[root_index]==workbook.ROOT_HEADER_KEY]

    # Now map root rows -> header dicts then make a dataframe and serialize it to xlsx????
    new_rows = []
    for row in root_rows:
        if len(row) != len(root_header):
            raise ValueError('Row length does not equal header length.')
        d = {k:v for k, v in zip(root_header, row)}
        new_rows.append(d)

    log.debug('Extracted {} root rows.'.format(len(new_rows)))

    return new_rows

# noinspection PyMissingOrEmptyDocstring
def main(options):  # pragma: no cover
    if not options.verbose:
        logging.disable(logging.DEBUG)
    log.info('Parsing {}'.format(options.input))
    r = ingest(fp=options.input)
    log.info('Dumping data from the first 10 rows as JSON.')
    print(json.dumps(r[:10], sort_keys=True, indent=4))
    sys.exit(0)


# noinspection PyMissingOrEmptyDocstring
def makeargpaser():  # pragma: no cover
    parser = argparse.ArgumentParser(description="Test parsing out root roows.")
    parser.add_argument('-i', '--input', dest='input', required=True, type=str, action='store',
                        help='Input file to process')
    parser.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true',
                        help='Enable verbose output')
    return parser


def _main():  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
    p = makeargpaser()
    opts = p.parse_args()
    main(opts)


if __name__ == '__main__':  # pragma: no cover
    _main()
