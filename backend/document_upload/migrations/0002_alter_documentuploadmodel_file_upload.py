# Generated by Django 4.2.4 on 2023-08-08 12:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentuploadmodel',
            name='file_upload',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'txt'])]),
        ),
    ]
