# Generated by Django 3.1.2 on 2020-11-08 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intern', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='Body',
        ),
    ]
