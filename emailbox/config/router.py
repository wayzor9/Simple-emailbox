from rest_framework import routers
from notifications.views import MailboxViewset, TemplateViewset, EmailViewset

router = routers.DefaultRouter()
router.register(r"mailbox", MailboxViewset)
router.register(r"template", TemplateViewset)
router.register(r"email", EmailViewset)
