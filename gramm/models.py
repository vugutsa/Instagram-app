from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =60)
    description = models.CharField(max_length =200)
    date = models.DateTimeField(auto_now_add=True)
    Images_image = models.ImageField(upload_to = 'images/')
    caption = models.CharField(max_length =60)
    profile= models.ForeignKey('profile', on_delete=models.CASCADE)


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)