# Generated by Django 4.2.5 on 2023-09-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_videochunk'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
