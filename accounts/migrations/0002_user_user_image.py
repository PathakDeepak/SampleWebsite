# Generated by Django 2.0.4 on 2018-04-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to=''),
        ),
    ]
