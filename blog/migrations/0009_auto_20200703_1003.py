# Generated by Django 3.0.7 on 2020-07-03 04:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200703_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 4, 33, 1, 271875, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
    ]
