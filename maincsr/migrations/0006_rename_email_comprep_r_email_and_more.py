# Generated by Django 4.0.4 on 2022-05-27 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maincsr', '0005_alter_companytable_phone_alter_comprep_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comprep',
            old_name='email',
            new_name='r_email',
        ),
        migrations.RenameField(
            model_name='comprep',
            old_name='phone',
            new_name='r_phone',
        ),
        migrations.RenameField(
            model_name='ngorep',
            old_name='email',
            new_name='r_email',
        ),
        migrations.RenameField(
            model_name='ngorep',
            old_name='phone',
            new_name='r_phone',
        ),
    ]
