from django.db import models

class contactDetails(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
# Create your models here.
