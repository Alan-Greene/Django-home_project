# Generated by Django 2.2.4 on 2019-09-29 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='descrition',
            new_name='description',
        ),
    ]