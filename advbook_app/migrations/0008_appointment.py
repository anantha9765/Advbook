# Generated by Django 4.2.6 on 2023-12-06 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advbook_app', '0007_adv_register_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('advocate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advbook_app.adv_register')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advbook_app.register')),
            ],
        ),
    ]
