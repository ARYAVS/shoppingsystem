# Generated by Django 2.2.5 on 2019-12-28 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c1', '0021_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='username',
        ),
    ]
