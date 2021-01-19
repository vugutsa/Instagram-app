from django.test import TestCase
from .models import Image,Profile,tags,Comment

class ImageTestClass(TestCase):
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_method(self):
        self.new_image.save_image()
        new_image = Image.objects.all()      
        self.assertTrue(len(new_image) >0)
        
    def test_delete_image(self):
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)
        
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id, 'image/test.jpg')
        changed_img = Image.objects.filter(image='image/test.jpg')
        self.assertTrue(len(changed_img) > 0)
        
        
class ProfileTestClass(TestCase):
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    def test_save_method(self):
        self.new_image.save_profile()
        new_profile = Profile.objects.all()      
        self.assertTrue(len(new_profile) >0)
        
    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)== 0)
        
    def test_update_image(self):
        self.new_profile.save_image()
        self.new_profile.update_image(self.new_profile.id)
        self.assertTrue(len(changed_profile) > 0)        