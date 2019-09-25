from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    discription=models.TextField(blank=True)