# Generated by Django 4.2.3 on 2023-08-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='newsImages/'),
        ),
    ]
