from django.db import models

# Create your models here.

class Image(models.Model):
    username=models.CharField(max_length=50)
    imgfile = models.ImageField(upload_to='images/%Y/%m/%d')
