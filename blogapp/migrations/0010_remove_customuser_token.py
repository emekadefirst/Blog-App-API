# Generated by Django 4.2.3 on 2023-10-04 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_customuser_token_delete_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='token',
        ),
    ]
