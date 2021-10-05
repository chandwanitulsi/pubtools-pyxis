Pyxis Client
=====================

.. py:module:: pubtools._pyxis.pyxis_client

Class for performing actual Pyxis queries and handling related logic.

.. autoclass:: PyxisClient

   .. automethod:: __init__
   .. automethod:: get_operator_indices
   .. automethod:: get_repository_metadata
   .. automethod:: upload_signatures
   .. automethod:: _do_parallel_requests
   .. automethod:: _handle_json_response
   .. automethod:: get_container_signatures
   .. automethod:: _get_items_from_all_pages
   .. automethod:: delete_container_signatures
