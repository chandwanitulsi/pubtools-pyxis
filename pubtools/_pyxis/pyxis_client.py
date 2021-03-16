from requests.exceptions import HTTPError

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

    def get_repository_metadata(
        self, repo_name, custom_registry=None, only_internal=False, only_partner=False
    ):
        """Get metadata of a Comet repository.

        If checking only one registry hasn't been specified, check both with precedence on
        the internal registry.

        Args:
            repo_name (str):
                Name of the repository.
            custom_registry (str):
                Use a custom registry address instead of the default ones.
            only_internal (bool):
                Whether to only check internal registry.
            only_partner (bool):
                Whether to only check partner registry.
        Returns (dict):
            Metadata of the repository.
        """
        internal_registry = "registry.access.redhat.com"
        partner_registry = "registry.connect.redhat.com"
        endpoint = "repositories/registry/{0}/repository/{1}"
        if custom_registry:
            resp = self.pyxis_session.get(endpoint.format(custom_registry, repo_name))
        elif only_internal:
            resp = self.pyxis_session.get(endpoint.format(internal_registry, repo_name))
        elif only_partner:
            resp = self.pyxis_session.get(endpoint.format(partner_registry, repo_name))
        else:
            resp = self.pyxis_session.get(endpoint.format(internal_registry, repo_name))
            # if 'not found' error, try another registry
            if resp.status_code == 404:
                resp = self.pyxis_session.get(
                    endpoint.format(partner_registry, repo_name)
                )

        resp.raise_for_status()
        return resp.json()

    def upload_signatures(self, signatures):
        """
        Upload signatures from given JSON string.

        Args:
            signatures (str)
                JSON with signatures to upload.  See Pyxis API for details.

        Returns:
            list: List of uploaded signatures including auto-populated fields.
        """
        headers = {
            "Content-Type": "application/json",
        }
        resp = self.pyxis_session.post("signatures", data=signatures, headers=headers)

        return self._parse_response(resp)

    def _parse_response(self, response):
        """
        Get JSON from given response or raise an informative exception.

        Uses `requests.raise_for_status()` but tries to extract more details.
        """
        # the response may contain useful JSON even in case of 40x/50x
        # but it can't be guaranteed
        try:
            data = response.json()
        except ValueError:  # Python 2.x compat
            data = {}

        try:
            response.raise_for_status()
        except HTTPError as e:
            # We've got an error, but by default the exception contains only
            # minimal information: status code (400) and reason (Client error).
            # If the JSON was successfully parsed earlier, it may contain
            # important details (e.g. "Maximum of 100 signatures are allowed").
            extra_msg = data["detail"] if "detail" in data else response.text

            # re-raise the exception with an extra message
            raise HTTPError("{0}\n{1}".format(e, extra_msg))

        return data

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
