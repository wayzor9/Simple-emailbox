import uuid

from django.contrib.postgres.fields import ArrayField
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.db import models
from django.utils import timezone


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

    def email_backend(self):
        return EmailBackend(
            host=self.host,
            port=self.port,
            username=self.login,
            password=self.password,
            use_tls=self.use_ssl,
        )


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=140)
    text = models.TextField()
    attachment = models.FileField(upload_to="uploads/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"subject: {self.subject}"


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.ForeignKey(
        Mailbox, on_delete=models.CASCADE, related_name="emails"
    )
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, related_name="emails"
    )
    to = ArrayField(models.EmailField(max_length=254))
    cc = ArrayField(models.EmailField(max_length=254), blank=True, default=list)
    bcc = ArrayField(models.EmailField(max_length=254), blank=True, default=list)
    reply_to = models.EmailField(max_length=254, blank=True, null=True)
    sent_date = models.DateTimeField(default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id}, {self.mailbox}"

    def send_email(self, fail_silenty=False):
        if self.mailbox.is_active:
            EmailMessage(
                subject=self.template.subject,
                body=self.template.text,
                from_email=self.mailbox.email_from,
                to=self.to,
                bcc=self.bcc,
                connection=self.mailbox.email_backend(),
                attachments=self.template.attachment,
                cc=self.cc,
                fail_silently=fail_silenty,
            ).send()
            self.send_date = timezone.now()
            self.save()
