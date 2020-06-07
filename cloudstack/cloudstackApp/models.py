from django.db import models

# Create your models here.
class UserSignup(models.Model):
	First_Name=models.CharField(max_length=30,default=False)
	Last_Name=models.CharField(max_length=30,default=False)
	Email=models.EmailField(max_length = 254,unique=True)
	Password =models.CharField(max_length=30,default=False)
	Profile_Image=models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	def __str__(self):
		return self.First_Name

