Upload container image signatures
=================================

.. py:module:: pubtools._pyxis.pyxis_ops

Upload new container image signatures to Pyxis. Signatures are specified in the JSON format. They can be specified directly as string to the invoked entrypoint, or as a file path, when prefixed with "@".

CLI reference
-------------

.. argparse::
   :module: pubtools._pyxis.pyxis_ops
   :func: set_upload_signatures_args
   :prog: pubtools-pyxis-upload-signatures

Signature JSON format
----------------------
The specific fields are generally expected to be filled by a different service.

.. code-block:: json

    [
        {
            "manifest_digest": "sha256:a1a1a1a1",
            "reference": "redhat.io/some-repository:1",
            "repository": "some-repository",
            "sig_key_id": "ABCDEFGH",
            "signature_data": "some-data"
        },
        {
            "manifest_digest": "sha256:b2b2b2b2",
            "reference": "stage.redhat.io/some-repository:1",
            "repository": "some-repository",
            "sig_key_id": "ABCDEFGH",
            "signature_data": "some-data"
        }
    ]

Examples
-------------

NOTE: The demonstration of various authentication types can be seen in "Get operator indices" entrypoint examples.

Upload signatures directly as a string:
::

  pubtools-pyxis-upload-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --signatures '[{"foo": "bar"}]'

Upload signatures by specifying a filepath containing the signatures JSON:
::

  pubtools-pyxis-upload-signatures \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --signatures @signatures.json