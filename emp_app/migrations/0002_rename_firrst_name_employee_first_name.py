# Generated by Django 4.1.3 on 2022-11-08 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='firrst_name',
            new_name='first_name',
        ),
    ]
