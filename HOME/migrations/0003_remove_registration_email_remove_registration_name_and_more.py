# Generated by Django 4.2.7 on 2023-11-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_rename_email_registration_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='EMAIL',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='NAME',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='PASSW',
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
