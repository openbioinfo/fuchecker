.. ctfusion documentation master file, created by
   sphinx-quickstart on Thu Oct 25 15:36:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
===============================================
Welcome to ctfusion's documentation!
===============================================

Introduction
============

ctfusion id used to find fuison in ctdna data

Authors
=======

.. _authors:
    - tuxn <tuxiaonian@genehe.com>

Status
======

.. note::

   **not reviewed yet.**

installation
===========

use git to clone code::

    git clone git@192.168.1.251:/home/git/ctfusion.git
    
Usage
=====

.. just_type_command::

    /path/to/ctfusion.py -h

must_args
---------

- i,--input=<sam>
    input sam files
- f,--fusion=<fusions>
    fusions list file
- p,--prefix=<prefix>
    output prefix
- o,--output=<path>
    output path


RUN
===
cli way
-------

    /path/of/ctpips.py -i sam -f fusion_file -p prefix -o output_path

Tests
=====

check test report `here <http://192.168.1.4700:/dev-tests/ctfusion/>`_

Report
======

check sample report `here <http://192.168.1.4700:/dev-report/ctfusion/html/>`_

Code
====

.. toctree::
   :maxdepth: 1

    Guide <index>
    Code Docs <api/modules>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
