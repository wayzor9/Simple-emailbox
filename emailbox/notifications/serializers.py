from rest_framework import serializers
from .models import Mailbox, Template, Email


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = (
            "id",
            "host",
            "port",
            "login",
            "password",
            "email_from",
            "use_ssl",
            "is_active",
        )


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = (
            "id",
            "subject",
            "text",
            "attachment",
        )


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            "id",
            "mailbox",
            "template",
            "to",
            "cc",
            "bcc",
            "reply_to",
            "sent_date",
        )
