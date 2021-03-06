# Generated by Django 3.1.4 on 2020-12-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0002_signaturekey_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="signaturekey",
            name="key_type",
            field=models.TextField(
                choices=[("primary", "Primary"), ("secondary", "Secondary")],
                default="primary",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
