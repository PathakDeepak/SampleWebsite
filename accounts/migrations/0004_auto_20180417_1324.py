# Generated by Django 2.0.4 on 2018-04-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180417_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='../static/upload/no-img.jpg', upload_to='../static/upload/'),
        ),
    ]