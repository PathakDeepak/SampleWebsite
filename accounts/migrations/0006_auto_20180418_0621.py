# Generated by Django 2.0.4 on 2018-04-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180417_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
