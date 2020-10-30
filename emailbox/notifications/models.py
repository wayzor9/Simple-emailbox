from django.contrib.postgres.fields import ArrayField
from django.db import models

import uuid


class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email_from = models.CharField(max_length=100)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def sent(self):
        return self.emails.count()

    def __str__(self):
        return f"id: {self.id}"


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=140)
    text = models.TextField()
    attachment = models.FileField(upload_to="uploads/")
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.id}, subject: {self.subject}"


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.ForeignKey(
        Mailbox, on_delete=models.CASCADE, related_name="emails"
    )
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, related_name="emails"
    )
    to = ArrayField(models.EmailField(max_length=254))
    cc = ArrayField(models.EmailField(max_length=254), default=list)
    bcc = ArrayField(models.EmailField(max_length=254), default=list)
    reply_to = models.EmailField(max_length=254, blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id}, {self.mailbox}"
