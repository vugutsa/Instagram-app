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

    @classmethod
    def search_by_name(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return image
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name    