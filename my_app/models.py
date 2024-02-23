from django.db import models
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class portfolio_model(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    description = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField()
    live_link = models.URLField()
    technology_used = models.ManyToManyField('technology_used', verbose_name='Technology Used', blank=True)

    
    def __str__(self):
        return self.title

class technology_used(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name