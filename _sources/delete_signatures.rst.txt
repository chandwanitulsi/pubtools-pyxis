Delete container image signatures
=================================

.. py:module:: pubtools._pyxis.pyxis_ops

Delete existing container image signatures with matching internal IDs.

The IDs can be gathered by using the pubtools-pyxis-get-signatures entrypoint. The reason for using internal IDs is to ensure the unambiguity of the to-be-removed signatures.

CLI reference
-------------

.. argparse::
   :module: pubtools._pyxis.pyxis_ops
   :func: set_delete_signatures_args
   :prog: pubtools-pyxis-delete-signatures


Examples
-------------

NOTE: The demonstration of various authentication types can be seen in "Get operator indices" entrypoint examples.

Get multiple signatures with specified IDs
::

  pubtools-pyxis-delete-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --ids sigid1,sigid2
