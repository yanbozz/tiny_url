# Generated by Django 3.2.15 on 2022-08-12 12:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shorteners', '0002_rename_creator_id_urls_creator'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Urls',
            new_name='Url',
        ),
    ]
