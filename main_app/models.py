from django.db import models

# Create your models here.
class Kdrama(models.Model):
  title = models.CharField(max_length=100)
  year = models.PositiveIntegerField()
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.title
