from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Kdrama, Award

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
  undeserved_awards = Award.objects.exclude(id__in = kdrama.awards.all().values_list('id'))
  return render(request, 'kdramas/detail.html', {'kdrama': kdrama, 'awards': undeserved_awards})

def assoc_award(request, kdrama_id, award_id):
  Kdrama.objects.get(id=kdrama_id).awards.add(award_id)
  return redirect('detail', kdrama_id=kdrama_id)

class AwardList(ListView):
  model = Award

class AwardDetail(DetailView):
  model = Award

class AwardCreate(CreateView):
  model = Award
  fields = '__all__'

class AwardUpdate(UpdateView):
  model = Award
  fields = ['adjective', 'category']

class AwardDelete(DeleteView):
  model = Award
  success_url = '/awards/'