# Generated by Django 3.1.4 on 2020-12-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_encryptionkey_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]