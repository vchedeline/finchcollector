from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Kdrama, Award, Photo
from .forms import WatchingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'finch-collector-cv-96'

# Create your views here.
class KdramaCreate(CreateView):
  model = Kdrama
  fields = ['title', 'year', 'genre', 'description']

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
  watching_form = WatchingForm()
  return render(request, 'kdramas/detail.html', {'kdrama': kdrama, 'awards': undeserved_awards, 'watching_form': watching_form})

def add_watching(request, kdrama_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.kdrama_id = kdrama_id
    new_watching.save()
  return redirect('detail', kdrama_id=kdrama_id)

def assoc_award(request, kdrama_id, award_id):
  Kdrama.objects.get(id=kdrama_id).awards.add(award_id)
  return redirect('detail', kdrama_id=kdrama_id)

def disassoc_award(request, kdrama_id, award_id):
  Kdrama.objects.get(id=kdrama_id).awards.remove(award_id)
  return redirect('detail', kdrama_id=kdrama_id)

def add_photo(request, kdrama_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        session = boto3.Session(profile_name='finch')
        s3 = session.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, kdrama_id=kdrama_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
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