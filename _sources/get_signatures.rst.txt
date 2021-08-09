Get container image signatures
=================================

.. py:module:: pubtools._pyxis.pyxis_ops

Get existing container image signatures from Pyxis. The signatures matching specified criteria will be fetched. 

The desired signatures can be filtered based on two criteria: manifest digest and image reference. Multiple values of each criterion can be specified as CSV. Both criteria may be used simultaneously, and an "OR" operator will be used between them (signatures matching either criterion will be returned).

CLI reference
-------------

.. argparse::
   :module: pubtools._pyxis.pyxis_ops
   :func: set_get_signatures_args
   :prog: pubtools-pyxis-get-signatures


Examples
-------------

NOTE: The demonstration of various authentication types can be seen in "Get operator indices" entrypoint examples.

Get signatures matching the specified manifest digests:
::

  pubtools-pyxis-get-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --manifest-digest sha256:a1a1a1a1,sha256:b2b2b2b2

Get signatures matching the specified image references:
::

  pubtools-pyxis-get-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --reference registry.com/namespace/image:1,registry.com/namespace/other-image:2

Get signatures matching the specified manifest digests OR image references:
::

  pubtools-pyxis-get-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --manifest-digest sha256:a1a1a1a1,sha256:b2b2b2b2
  --reference registry.com/namespace/image:1,registry.com/namespace/other-image:2,