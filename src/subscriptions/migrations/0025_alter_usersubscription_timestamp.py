# Generated by Django 5.0.6 on 2024-08-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0024_usersubscription_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
