"""Stream type classes for tap-mailerlite."""

from typing import Any, Dict, Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import MailerLiteStream


class SubscribersStream(MailerLiteStream):
    """Defines Subscribers Stream."""

    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("email", th.StringType),
        th.Property("name", th.StringType),
        th.Property("sent", th.IntegerType),
        th.Property("opened", th.IntegerType),
        th.Property("opened_rate", th.NumberType),
        th.Property("clicked", th.IntegerType),
        th.Property("clicked_rate", th.NumberType),
        th.Property("type", th.StringType),
        th.Property("country_id", th.StringType),
        th.Property("signup_ip", th.StringType),
        th.Property("signup_timestamp", th.DateTimeType),
        th.Property("confirmation_ip", th.StringType),
        th.Property("confirmation_timestamp", th.DateTimeType),
        th.Property(
            "fields",
            th.ArrayType(
                th.ObjectType(
                    th.Property("key", th.StringType),
                    th.Property("value", th.StringType),
                    th.Property("type", th.StringType),
                )
            ),
        ),
        th.Property("date_subscribe", th.DateType),
        th.Property("date_unsubscribe", th.DateTimeType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_updated", th.DateTimeType),
    ).to_dict()


class SubscribersGroupsStream(MailerLiteStream):
    """Defines Subscribers Groups Stream."""

    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("total", th.IntegerType),
        th.Property("active", th.IntegerType),
        th.Property("unsubscribed", th.IntegerType),
        th.Property("bounced", th.IntegerType),
        th.Property("unconfirmed", th.IntegerType),
        th.Property("junk", th.IntegerType),
        th.Property("sent", th.IntegerType),
        th.Property("opened", th.IntegerType),
        th.Property("clicked", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_updated", th.DateTimeType),
    ).to_dict()


class CampaingnsStream(MailerLiteStream):
    """Defines Campaingns stream."""

    name = "campaigns"
    path = "/campaigns/{status}"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("total_recipients", th.IntegerType),
        th.Property("type", th.StringType),
        th.Property("date_created", th.StringType),
        th.Property("date_send", th.StringType),
        th.Property("name", th.StringType),
        th.Property("subject", th.StringType),
        th.Property("status", th.StringType),
        th.Property(
            "opened",
            th.ObjectType(
                th.Property("count", th.IntegerType),
                th.Property("rate", th.NumberType),
            ),
        ),
        th.Property(
            "clicked",
            th.ObjectType(
                th.Property("count", th.IntegerType),
                th.Property("rate", th.NumberType),
            ),
        ),
    ).to_dict()
