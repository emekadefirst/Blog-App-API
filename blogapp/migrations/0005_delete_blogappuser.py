# Generated by Django 4.2.3 on 2023-10-04 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blogappuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogAppUser',
        ),
    ]
