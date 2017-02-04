========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/rhizopathy/badge/?style=flat
    :target: https://readthedocs.org/projects/rhizopathy
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/williamgibb/rhizopathy.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/williamgibb/rhizopathy

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/williamgibb/rhizopathy?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/williamgibb/rhizopathy

.. |requires| image:: https://requires.io/github/williamgibb/rhizopathy/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/williamgibb/rhizopathy/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/williamgibb/rhizopathy/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/williamgibb/rhizopathy

.. |landscape| image:: https://landscape.io/github/williamgibb/rhizopathy/master/landscape.svg?style=flat
    :target: https://landscape.io/github/williamgibb/rhizopathy/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/rhizopathy.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/rhizopathy

.. |commits-since| image:: https://img.shields.io/github/commits-since/williamgibb/rhizopathy/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/williamgibb/rhizopathy/compare/v0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/rhizopathy.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/rhizopathy

.. |wheel| image:: https://img.shields.io/pypi/wheel/rhizopathy.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/rhizopathy

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rhizopathy.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/rhizopathy

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rhizopathy.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/rhizopathy


.. end-badges

Procesing tools for Winrhizotron data.

* Free software: BSD license

Installation
============

::

    pip install rhizopathy

Documentation
=============

https://rhizopathy.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
