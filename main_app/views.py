from django.shortcuts import render
from django.http import HttpResponse
from .models import Kdrama
# class Kdrama:
#   def __init__(self, title, year, genre, description):
#     self.title = title
#     self.year = year
#     self.genre = genre
#     self.description = description

# kdramas = [
#   Kdrama('Boys over Flowers', 2009, 'Romantic', 'Unassuming high school girl Jan-di stands up to -- and eventually falls for -- a spoiled rich kid who belongs to the school''s most powerful clique'),
#   Kdrama('My Secret Romance', 2017, 'Romantic', 'Jin Wook, a rich playboy set to inherit his dad''s company, has a chance encounter with Yoo Mi, who has more modest ambitions to become a nutritionist'),
#   Kdrama('Inheritors', 2013, 'Romantic', 'After a chance encouter in LA, two teens from different social backgrounds reunite at an exclusive high school attended by Korea''s uber rich'),
#   Kdrama('Love Alarm', 2021, 'Romantic', 'In a world where an app alerts people if someone in the vicinity likes them, Kim Jojo experiences young love while coping with personal adversities')
# ]

# Create your views here.
def home(request):
 return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def kdramas_index(request):
  kdramas = Kdrama.objects.all()
  return render(request,'kdramas/index.html', {'kdramas': kdramas})