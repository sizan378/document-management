# Generated by Django 4.2.4 on 2023-08-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField()),
                ('format', models.CharField(choices=[('pdf', 'Pdf'), ('docx', 'Docx'), ('txt', 'Txt')], max_length=50)),
                ('file_upload', models.FileField(upload_to='')),
                ('user', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
