from django.db import models

# Create your models here.
class job(models.model):
    image = models.ImageField(upload_to='')
    summery = models.CharField(max_length=200)