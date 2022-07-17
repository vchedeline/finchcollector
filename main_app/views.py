from django.shortcuts import render
from django.http import HttpResponse
from .models import Kdrama

# Create your views here.
def home(request):
 return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def kdramas_index(request):
  kdramas = Kdrama.objects.all()
  return render(request,'kdramas/index.html', {'kdramas': kdramas})

def kdrama_detail(request, kdrama_id):
  kdrama = Kdrama.objects.get(id=kdrama_id)
  return render(request, 'kdramas/detail.html', {'kdrama': kdrama})