from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_description = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title', unique=True, null=True, default=None)
    news_file = models.FileField(upload_to="newsImages/", max_length=250, null=True, default=None)


# Create your models here.
