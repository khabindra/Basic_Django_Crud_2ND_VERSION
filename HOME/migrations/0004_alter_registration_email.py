# Generated by Django 4.2.7 on 2023-11-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0003_remove_registration_email_remove_registration_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
