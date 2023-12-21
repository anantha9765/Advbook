# Generated by Django 4.2.6 on 2023-11-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advbook_app', '0004_alter_register_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
                ('image', models.ImageField(default='null.jpg', upload_to='imgfile')),
                ('edu_details', models.CharField(max_length=50)),
                ('edu_proof', models.ImageField(default='null.jpg', upload_to='imgfile')),
                ('password', models.CharField(max_length=30)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
