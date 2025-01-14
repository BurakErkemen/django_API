from django.db import models

# Video model
class Video(models.Model):
    title = models.CharField(max_length=100)
    videoURL = models.FileField(upload_to='videos/')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    title = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='images/')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
