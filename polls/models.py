from django.db import models

# Create your models here.
class Note(models.Model):
    title= models.CharField(max_length=100)
    date_added=models.DateTimeField('date added', auto_now_add=True)
    note=models.TextField()
    category = models.CharField(max_length= 39,
default='teaching')

    def __str__(self):
        return self.title

