# Generated by Django 2.0.4 on 2018-04-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180418_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
