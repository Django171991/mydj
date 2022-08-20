from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images')
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title