===============
 pubtools-pyxis
===============

Set of scripts used for operating with Pyxis service.


Requirements
============

* Python 2.6+
* Python 2.7+
* Python 3.7+

Features
========

pubtools-pyxis-get-operator-indices - get a list of index images satisfying the specified conditions
pubtools-pyxis-get-repo-metadata - get metadata of a Comet repo
pubtools-pyxis-upload-signatures - upload container signatures to Pyxis

Setup
=====

::

  $ pip install -r requirements.txt
  $ pip install .
  or
  $ python setup.py install

Usage
=====

Get operator indices:
::

  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-krb-principal lgallovi@REDHAT.COM \
  --ocp-versions-range 4.6 \
  --pyxis-insecure

  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-krb-principal iib-stage@REDHAT.COM \
  --pyxis-krb-ktfile /path/to/file.keytab \
  --ocp-versions-range 4.5-4.7

  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --ocp-versions-range 4.6

Get repository metadata:
::

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name \
  --only-internal-registry

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name \
  --only-partner-registry

Upload signatures:
::

  pubtools-pyxis-upload-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --signatures '[{"foo": "bar"}]'

  pubtools-pyxis-upload-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --signatures @signatures.json

Get signatures:
::

  pubtools-pyxis-get-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --manifest-digest sha256-digest-of-manifest,sha256-digest-of-other-manifest

  pubtools-pyxis-get-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --manifest-digest sha256-digest-of-manifest
  --reference pull-reference-of-image,pull-reference-of-image2

