from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50,unique=True)
    user_pass = models.CharField(max_length=264)
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=30)
    user_contact = models.IntegerField()
    user_email = models.EmailField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=30)
    user_image = models.ImageField(upload_to='profile_images', blank=True,default='profile_image/default.png' )

