# Generated by Django 3.1.4 on 2021-02-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210218_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(auto_created=True, max_length=30)),
                ('user_email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
