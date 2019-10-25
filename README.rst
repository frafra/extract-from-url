.. image:: https://img.shields.io/pypi/v/extract_from_url.svg
    :target: https://pypi.org/project/extract_from_url/

Description
===========
    
Take advantage of `libarchive <https://libarchive.org/>`_ to download and extract files without having to store the archive first. Works with ZIP files too!

Dependencies
============

1. `libarchive-c <https://pypi.org/project/libarchive-c/>`_ which requires ``libarchive-devel`` or ``libarchive-dev`` to be built
2. `tqdm <https://pypi.org/project/tqdm/>`_ for progress bars

You can use `poetry <https://poetry.eustace.io/>`_ or `pip <https://pip.pypa.io/>`_ to install the dependencies.

Usage
=====

As standalone program
---------------------

Please see ``cli.py --help``

As library
----------

Available as package on `PyPI <https://pypi.org/project/extract-from-url/>`_.
