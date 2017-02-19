# -*- coding: utf-8 -*-
"""
rhizopathy - exc.py
Created on 2/8/17.

Exception definitions.
"""


# XXX These ALL need docstrings!
class AnalyzerError(Exception):
    pass


class DataError(AnalyzerError):
    pass


class SerializationError(AnalyzerError):
    pass


class FieldsError(Exception):
    pass

class TubeError(Exception):
    pass
