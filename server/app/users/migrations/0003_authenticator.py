# Generated by Django 2.1.7 on 2019-03-12 22:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190312_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authenticator', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 12, 22, 45, 33, 949383, tzinfo=utc))),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
    ]