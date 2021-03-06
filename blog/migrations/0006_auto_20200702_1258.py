# Generated by Django 3.0.7 on 2020-07-02 07:28

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200702_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 7, 28, 40, 458465, tzinfo=utc)),
        ),
    ]
