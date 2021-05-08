# Generated by Django 3.2.2 on 2021-05-08 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_auto_20210508_1310"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teamacmeaccount",
            old_name="private_key",
            new_name="jwk",
        ),
        migrations.RemoveField(
            model_name="teamacmeaccount",
            name="public_key",
        ),
    ]
