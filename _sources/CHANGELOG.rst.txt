ChangeLog
=========

1.3.7 (2025-05-06)
------------------

* python3.9 compatibility fixes

1.3.6 (2025-03-06)
------------------

* Splitted entrypoitnts to `console_scripts` and `mod`.


1.3.5 (2023-03-14)
------------------

* Delete signatures in parallel

1.3.4 (2023-03-01)
------------------

* Fix request threads
* Drop Python 2 support

1.3.3 (2022-11-09)
------------------

* Tolerate 409 of signature upload
* Add Bandit checks and resolve Bandit findings

1.3.2 (2021-10-15)
------------------

* Modified the retry requests approach

1.3.1 (2021-08-19)
------------------

* Fixed building with Python 2.6 distutils

1.3.0 (2021-08-18)
------------------

* Added documentation
* Added support for parallel uploading of signatures

1.2.0 (2021-06-10)
------------------

* Added the ability to add file as input type for --manifest_digests and --reference for get-signatures
* Added entrypoint for removing signatures

1.1.0 (2021-03-29)
------------------

* Added upload-signatures, get-signatures to interact with pyxis sigstore
* Added get-repository-metadata to fetch repository data from pyxis
* Fixed py2.6 pip url

1.0.0 (2020-11-27)
------------------

* Set version to 1.0.0 to indicate stable release

0.2.0 (2020-11-23)
------------------

* Fix module path


0.1.0 (2020-11-20)
------------------

* Initial release.

