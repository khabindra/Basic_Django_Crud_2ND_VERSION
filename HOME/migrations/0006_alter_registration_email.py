# Generated by Django 4.2.7 on 2023-11-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_alter_registration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]
