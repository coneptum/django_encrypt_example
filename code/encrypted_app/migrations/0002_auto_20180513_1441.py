# Generated by Django 2.0.5 on 2018-05-13 14:41

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encrypted_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelwithsomeencryptedfields',
            name='encrypted_field',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
    ]
