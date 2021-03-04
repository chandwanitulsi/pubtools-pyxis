from .pyxis_session import PyxisSession


# pylint: disable=bad-option-value,useless-object-inheritance
class PyxisClient(object):
    """Pyxis requests wrapper."""

    def __init__(
        self,
        hostname,
        retries=3,
        auth=None,
        backoff_factor=2,
        verify=True,
    ):
        """
        Initialize.

        Args:
            hostname (str)
                Pyxis service hostname.
            retries (int)
                number of http retries for Pyxis requests.
            auth (PyxisAuth)
                PyxisAuth subclass instance.
            backoff_factor (int)
                backoff factor to apply between attempts after the second try.
            verify (bool)
                enable/disable SSL CA verification.
        """
        self.pyxis_session = PyxisSession(
            hostname, retries=retries, backoff_factor=backoff_factor, verify=verify
        )
        if auth:
            auth.apply_to_session(self.pyxis_session)

    def get_operator_indices(self, ocp_versions_range, organization=None):
        """Get a list of index images satisfying versioning and organization conditions.

        Args:
            ocp_versions_range (str)
                Supported OCP versions range.
            organization (str)
                Organization understood by IIB.

        Returns:
            list: List of index images satisfying the conditions.
        """
        params = {"ocp_versions_range": ocp_versions_range}
        if organization:
            params["organization"] = organization
        resp = self.pyxis_session.get("operators/indices", params=params)
        resp.raise_for_status()

        return resp.json()["data"]

    def get_container_signatures(self, manifest_digests, references, sig_key_ids):
        """Get a list of signature metadata matching given fields.

        Args:
            manifest_digests (comma seperated str)
                manifest_digest used for searching in signatures.
            references (comma seperated str)
                pull reference for image of signature stored.
            sig_key_ids (comma seperated str)
                signature id used to create signature

        Returns:
            list: List of signature metadata matching given fields.
        """
        signatures_url = "signatures"
        filter_urls = []
        if manifest_digests:
            filter_urls.append("manifest_digest=in=({}),".format(manifest_digests))
        if references:
            filter_urls.append("reference=in=({}),".format(references))
        if sig_key_ids:
            filter_urls.append("sig_key_id=in=({}),".format(sig_key_ids))

        if filter_urls:
            signatures_url = "{}{}".format(signatures_url, "?filter=")
            for filter_url in filter_urls:
                signatures_url = "{}{}".format(signatures_url, filter_url)
            signatures_url = signatures_url[0:-1]

        resp = self.pyxis_session.get(signatures_url)
        resp.raise_for_status()

        return resp.json()["data"]
