# Generated by Django 3.1.5 on 2021-02-06 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20210103_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSchemaTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('field', 'Form Field'), ('section', 'Form Section')], default='section', max_length=10)),
                ('schema', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FormSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('schema', models.TextField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schemas', to='forms.form')),
            ],
        ),
        migrations.AddConstraint(
            model_name='formschema',
            constraint=models.UniqueConstraint(fields=('key', 'form'), name='unique_key_per_form'),
        ),
    ]