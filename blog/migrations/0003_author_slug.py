# Generated by Django 3.0.3 on 2020-02-06 19:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200206_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.CharField(default=uuid.uuid4, max_length=61),
        ),
    ]
