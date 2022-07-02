"""REST client handling, including MailerLiteStream base class."""

from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.streams import RESTStream


class MailerLiteStream(RESTStream):
    """MailerLite stream class."""

    url_base = "https://api.mailerlite.com/api/v2"

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="X-MailerLite-ApiKey",
            value=self.config.get("api_key"),
            location="header",
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers
