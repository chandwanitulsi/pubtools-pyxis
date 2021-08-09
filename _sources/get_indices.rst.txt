Get operator indices
====================

.. py:module:: pubtools._pyxis.pyxis_ops

Get a list of index images satisfying the specified conditions

CLI reference
-------------

.. argparse::
   :module: pubtools._pyxis.pyxis_ops
   :func: set_get_operator_indices_args
   :prog: pubtools-pyxis-get-operator-indices

Examples
-------------

Get operator indices with one specified version and default Kerberos authentication.
::

  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-krb-principal lgallovi@REDHAT.COM \
  --ocp-versions-range 4.6 \
  --pyxis-insecure

Get operator indices with a version range, and Kerberos authentication with a specified keytab.
::
  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-krb-principal iib-stage@REDHAT.COM \
  --pyxis-krb-ktfile /path/to/file.keytab \
  --ocp-versions-range 4.5-4.7

Get operator indices and authenticate using SSL certificates.
::
  pubtools-pyxis-get-operator-indices \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --ocp-versions-range 4.6