from django.db import models

# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=255)
    Age=models.IntegerField()
    Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    email=models.CharField(max_length=255)
    dob=models.CharField(max_length=255)
    phone=models.IntegerField() 