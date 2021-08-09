===============
 pubtools-pyxis
===============

Set of scripts used for operating with Pyxis service. The scripts are mostly thin wrappers around the REST requests, solving mainly authentication, pagination, and minor data modification.

Kerberos and SSL based authentication is supported. The purpose of the library is not to create a wrapper around every Pyxis endpoint, only those utilized in pub-related tooling.

Requirements
============

* Python 2.6+
* Python 3.6+

Features
========

* pubtools-pyxis-get-operator-indices - Get a list of index images satisfying the specified conditions
* pubtools-pyxis-get-repo-metadata - Get metadata of the specified repository
* pubtools-pyxis-upload-signatures - Upload new container image signatures to Pyxis
* pubtools-pyxis-get-signatures - Get existing container image signatures based on the specified criteria
* pubtools-pyxis-delete-signatures - Delete existing container image signatures with matching internal IDs
Setup
=====

::

  $ pip install -r requirements.txt
  $ pip install . 
  or
  $ python setup.py install
