# Generated by Django 5.1 on 2024-12-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capstone', '0015_alter_comment_review_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='coordinates',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
