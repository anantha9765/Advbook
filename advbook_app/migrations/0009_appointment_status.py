# Generated by Django 4.2.6 on 2023-12-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advbook_app', '0008_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='Requested', max_length=100),
        ),
    ]
