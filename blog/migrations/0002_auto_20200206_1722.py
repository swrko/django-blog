# Generated by Django 3.0.3 on 2020-02-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='blogs',
            field=models.ManyToManyField(blank=True, related_name='authors', to='blog.Blog'),
        ),
    ]
