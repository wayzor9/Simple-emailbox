import django_filters
from rest_framework import viewsets

from .models import Mailbox, Template, Email
from .serializers import MailboxSerializer, TemplateSerializer, EmailSerializer


class MailboxViewset(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


class TemplateViewset(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class SentEmailFilterSet(django_filters.FilterSet):
    sent = django_filters.BooleanFilter(field_name="sent_date", lookup_expr="isnull")
    date = django_filters.DateTimeFilter(field_name="sent_date")

    class Meta:
        model = Email
        fields = ["sent", "date"]


class EmailViewset(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    http_method_names = ["get", "post"]
    filterset_class = SentEmailFilterSet
