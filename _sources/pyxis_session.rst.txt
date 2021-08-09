Pyxis Session
=====================

.. py:module:: pubtools._pyxis.pyxis_session

Class used for maintaining authentication credentials and various configuration options such as retries.

Instance of this class is used as a parameter for 'apply_to_session' authentication method.

.. autoclass:: PyxisSession

   .. automethod:: __init__
   .. automethod:: get
   .. automethod:: post
   .. automethod:: put
   .. automethod:: delete
   .. automethod:: _api_url
