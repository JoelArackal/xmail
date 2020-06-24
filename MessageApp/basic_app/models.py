from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Messages(models.Model):
    
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    MImage = models.ImageField(upload_to='images',blank=True)
    MFile = models.FileField(upload_to='files', blank=True)
    receiver = models.ForeignKey(User,related_name='received_messages', on_delete=models.CASCADE)
    sent_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.text)[0:5]+'.......'

   

