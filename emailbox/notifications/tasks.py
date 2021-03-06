from smtplib import SMTPException

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Email

logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_email_task(self, email_pk):
    email = Email.objects.get(id=email_pk)
    try:
        email.send_mail()
        logger.info("Email sent")
    except SMTPException as exc:
        logger.error(exc, exc_info=True)
        self.retry(exc=exc, max_retries=3)
