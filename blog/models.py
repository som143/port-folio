from django.db import models

class blog(models.Model):
    blog_image= models.ImageField(upload_to='images/')
    blog_title = models.CharField(max_length=200)
    blog_date = models.DateField()
    body = models.CharField(max_length=300)