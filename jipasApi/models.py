from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title= models.CharField(max_length=100)
    date_added=models.DateTimeField('date added', auto_now_add=True)
    note=models.TextField()
    category = models.CharField(max_length= 39,
default='teaching')

    def __str__(self):
        return self.title
class Comment(models.Model):
    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    owner =models.ForeignKey(User, related_name='comment',on_delete=models.CASCADE ,null=True)
    comment=models.TextField(unique=True)
    date_added=models.DateTimeField('date added', auto_now_add=True)
    likes=models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Image(models.Model):
    title= models.CharField(max_length=100)
    date_added=models.DateTimeField('date added', auto_now_add=True)
    description=models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.CharField(max_length= 39,
default='project')

    def __str__(self):
        return self.title

  