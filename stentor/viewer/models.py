from django.db import models

# Create your models here

class Channel(models.Model):

     channel_name = models.CharField(max_length = 50)
     channel_url = models.CharField(max_length = 100)

     def publish(self):
          self.save()

     def __str__(self):
          return self.channel_name
