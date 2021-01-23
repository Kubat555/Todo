from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length = 100)
    create_at =models.DateTimeField(auto_now_add = True)
    is_done = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length= 6)
    date = models.DateField(auto_now_add = True)
    is_favorite = models.BooleanField(default=False)

