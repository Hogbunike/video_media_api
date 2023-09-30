# Generated by Django 4.2.5 on 2023-09-29 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('is_playing', models.BooleanField(default=False)),
                ('last_played', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
