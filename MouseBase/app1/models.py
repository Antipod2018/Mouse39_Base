from django.db import models

# Create your models here.

class notebook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title