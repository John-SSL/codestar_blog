# Generated by Django 4.2.23 on 2025-06-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
