from django.db import models

# Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)
    
