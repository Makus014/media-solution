# Generated by Django 5.2 on 2025-04-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_databaseconnector_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseconnector',
            name='trend_explanation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='databaseconnector',
            name='trend_score',
            field=models.IntegerField(default=0),
        ),
    ]
