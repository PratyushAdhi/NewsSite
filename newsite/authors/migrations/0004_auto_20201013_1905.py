# Generated by Django 3.1.2 on 2020-10-13 19:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_author_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='followers',
            field=models.ManyToManyField(related_name='_author_followers_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
