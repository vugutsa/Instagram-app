# from django.test import TestCase
# from .models import Image,Profile,tags,Follow
# import datetime as dt
# # Create your tests here.

# class ImageTestClass(TestCase):
    
#     def setUp(self):

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_image,Image))
        
#     def test_save_method(self):
#         self.new_image.save_image()
#         new_image = Image.objects.all()      
#         self.assertTrue(len(new_image) >0)
        
#     def test_delete_image(self):
#         self.new_image.delete_image()
#         image = Image.objects.all()
#         self.assertTrue(len(image)== 0)
        
#     def test_update_image(self):
#         self.new_image.save_image()
#         self.new_image.update_image(self.new_image.id, 'image/test.jpg')
#         changed_img = Image.objects.filter(image='image/test.jpg')
#         self.assertTrue(len(changed_img) > 0)
        

        
# class LocationTestClass(TestCase):
    
#     # Set up method
#     def setUp(self):
#         self.location = Location(id=1,name = 'Nairobi')
        
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.location,Location))
        
#     # Testing Save Method
#     def test_save_method(self):
#         self.location.save_location()
#         location = Location.objects.all()
#         self.assertTrue(len(location) > 0)

#     def test_delete_location(self):
#         self.location.delete_location()
#         location = Location.objects.all()
#         self.assertTrue(len(location)== 0) 
        
#     def test_update_location(self):
#         self.location.save_location()
#         self.location.update_location(self.location.id, 'Mombasa')
#         changed_location = Location.objects.filter(name ='Mombasa')
#         self.assertTrue(len(changed_location) > 0)   
        
#     def tearDown(self):
#         Image.objects.all().delete()
#         Profile.objects.all().delete()
#         tags.objects.all().delete()   
                       