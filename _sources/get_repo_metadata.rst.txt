Get repository metadata
=======================

.. py:module:: pubtools._pyxis.pyxis_ops

Get metadata of the specified repository in Comet. Comet is a service which contains metadata related serving Red Hat container images to customers.

The entrypoint offers options of which registry should be checked. The default behavior is that internal registry is checked first, followed by the partner registry. If it's desired to check only one of these registries, it may be specified via argument. Lastly, a custom registry may be specified too, which will be the only checked registry.

CLI reference
-------------

.. argparse::
   :module: pubtools._pyxis.pyxis_ops
   :func: set_get_repo_metadata_args
   :prog: pubtools-pyxis-get-repo-metadata

Examples
-------------

NOTE: The demonstration of various authentication types can be seen in "Get operator indices" entrypoint examples.

Get repository metadata without specifying any registry options. Internal registry, followed by partner registry will be checked.
::

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name

Only check internal registry when gathering repo metadata.
::

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name \
  --only-internal-registry

Only check partner registry when gathering repo metadata.
::

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name \
  --only-partner-registry

Specify a custom registry.
::

  pubtools-pyxis-get-repo-metadata \
  --pyxis-server https://pyxis-server-url/ \
  --pyxis-ssl-crtfile /path/to/file.crt \
  --pyxis-ssl-keyfile /path/to/file.key \
  --repo-name some-repo/name \
  --custom-registry some.registry.redhat.com