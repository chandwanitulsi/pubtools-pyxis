Pyxis Authentication
=====================

.. py:module:: pubtools._pyxis.pyxis_authentication

Classes used for authenticating with Pyxis. Each class performs a different authentication type. Inheritence of the base class, PyxisAuth is used to ensure that the required methods have been implemented.

The method 'apply_to_session' applies the authentication to the Session object. It should generally be the only method that needs to be used.

Currently, two authentication types are supported: Kerberos and SSL.

Base class signature
---------------------
The base class dictates which methods must be implemented in the children classes.

.. autoclass:: PyxisAuth

   .. automethod:: __init__
   .. automethod:: apply_to_session

Children classes
----------------
These classes perform the actual authentication. More may be added if different authentication type is required.

.. autoclass:: PyxisSSLAuth

   .. automethod:: __init__
   .. automethod:: apply_to_session

.. autoclass:: PyxisKrbAuth

   .. automethod:: __init__
   .. automethod:: apply_to_session
   .. automethod:: _krb_auth