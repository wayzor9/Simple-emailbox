from django.utils import timezone

from rest_framework import serializers

from .models import Mailbox, Template, Email
from .tasks import send_email_task


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
    sent_date = serializers.DateTimeField(
        default=serializers.CreateOnlyDefault(timezone.now)
    )

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

    def create(self, validated_data):
        obj = super().create(validated_data)
        send_email_task.delay(obj.pk)
        return obj
