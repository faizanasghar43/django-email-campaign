from django.core.mail import send_mail, send_mass_mail
from django_q.tasks import async_task
from .models import Campaign


def send_campaign_email(campaign_id, email_list):
    campaign = Campaign.objects.get(id=campaign_id)
    recipients = email_list  # Provide the email list to send the campaign to
    subject = campaign.title
    message = campaign.description
    sender = 'your_email@example.com'  # Set the sender's email address
    send_mail(subject, message, sender, recipients)
