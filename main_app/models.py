from django.db import models
from django.urls import reverse

# Create your models here.
class Kdrama(models.Model):
  title = models.CharField(max_length=100)
  year = models.PositiveIntegerField()
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'kdrama_id': self.id})