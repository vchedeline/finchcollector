from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Kdrama

# Create your views here.
class KdramaCreate(CreateView):
  model = Kdrama
  fields = '__all__'

class KdramaUpdate(UpdateView):
  model = Kdrama
  fields = ['title', 'year', 'genre', 'description']

class KdramaDelete(DeleteView):
  model = Kdrama
  success_url = '/kdramas/'

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