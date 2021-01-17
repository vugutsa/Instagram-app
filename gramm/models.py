from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =60)
    # description = models.CharField(max_length =200)
    pub_date = models.DateTimeField(auto_now_add=True)
    Images_image = models.ImageField(upload_to = 'images/')
    caption = models.CharField(max_length =60)
    profile= models.ForeignKey('profile', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete
        
    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image
         
    @classmethod
    def update_caption(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.image_name
       


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)
    name = models.CharField(max_length =60)

    @classmethod
    def search_by_name(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photo
    def __str__(self):
        return self.name  
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name    
    
class GrammLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()    
    
class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User,related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)    