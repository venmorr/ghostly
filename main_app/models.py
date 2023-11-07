from django.db import models
from django.urls import reverse

class Ghost(models.Model):
  name = models.CharField(max_length=100)
  level = models.IntegerField()
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('ghost-detail', kwargs={'ghost_id': self.id})