# Generated by Django 2.2.5 on 2019-12-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c1', '0008_book3_usr'),
    ]

    operations = [
        migrations.CreateModel(
            name='users2',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contactno', models.IntegerField()),
                ('password', models.IntegerField()),
                ('DOB', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='users1',
        ),
    ]
