# Generated by Django 4.2.3 on 2023-07-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_remove_campaign_emails_campaign_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='email',
        ),
        migrations.AddField(
            model_name='campaign',
            name='found_email',
            field=models.EmailField(default='contact@synares.com', max_length=254),
            preserve_default=False,
        ),
    ]
