from django.db import models
from django.urls import reverse
from datetime import date

STARS = (
  ('5', 'Five Stars'),
  ('4', 'Four Stars'),
  ('3', 'Three Stars'),
  ('2', 'Two Stars'),
  ('1', 'One Stars')
)

# Create your models here.
class Award(models.Model):
  adjective = models.CharField(max_length=100)
  category = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.adjective} {self.category}'

  def get_absolute_url(self):
    return reverse('award_detail', kwargs={'pk': self.id})

class Kdrama(models.Model):
  title = models.CharField(max_length=100)
  year = models.PositiveIntegerField()
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  awards = models.ManyToManyField(Award)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'kdrama_id': self.id},)

  def watched_episode_today(self):
    return self.watching_set.filter(date=date.today()).count() >= 1

class Watching(models.Model):
  date = models.DateField('Watch Date')
  episodes = models.PositiveSmallIntegerField('Episodes Watched')
  stars = models.CharField(max_length=1, choices=STARS, default=STARS[0][0])
  kdrama = models.ForeignKey(Kdrama, on_delete=models.CASCADE)

  def __str__(self):
    return f'Watched {self.episodes} on {self.date}, Rating: {self.get_stars_display()}'

  class Meta:
    ordering = ['-date']