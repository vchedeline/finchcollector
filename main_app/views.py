from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Kdrama, Award, Photo
from .forms import WatchingForm
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'finch-collector-cv-96'

# Create your views here.
class KdramaCreate(LoginRequiredMixin, CreateView):
  model = Kdrama
  fields = ['title', 'year', 'genre', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class KdramaUpdate(LoginRequiredMixin, UpdateView):
  model = Kdrama
  fields = ['title', 'year', 'genre', 'description']

class KdramaDelete(LoginRequiredMixin, DeleteView):
  model = Kdrama
  success_url = '/kdramas/'

def home(request):
 return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def kdramas_index(request):
  kdramas = Kdrama.objects.filter(user=request.user)
  return render(request,'kdramas/index.html', {'kdramas': kdramas})

@login_required
def kdrama_detail(request, kdrama_id):
  kdrama = Kdrama.objects.get(id=kdrama_id)
  undeserved_awards = Award.objects.exclude(id__in = kdrama.awards.all().values_list('id'))
  watching_form = WatchingForm()
  return render(request, 'kdramas/detail.html', {'kdrama': kdrama, 'awards': undeserved_awards, 'watching_form': watching_form})

@login_required
def add_watching(request, kdrama_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.kdrama_id = kdrama_id
    new_watching.save()
  return redirect('detail', kdrama_id=kdrama_id)

@login_required
def assoc_award(request, kdrama_id, award_id):
  Kdrama.objects.get(id=kdrama_id).awards.add(award_id)
  return redirect('detail', kdrama_id=kdrama_id)

@login_required
def disassoc_award(request, kdrama_id, award_id):
  Kdrama.objects.get(id=kdrama_id).awards.remove(award_id)
  return redirect('detail', kdrama_id=kdrama_id)

@login_required
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

class AwardList(LoginRequiredMixin, ListView):
  model = Award

class AwardDetail(LoginRequiredMixin, DetailView):
  model = Award

class AwardCreate(LoginRequiredMixin, CreateView):
  model = Award
  fields = '__all__'

class AwardUpdate(LoginRequiredMixin, UpdateView):
  model = Award
  fields = ['adjective', 'category']

class AwardDelete(LoginRequiredMixin, DeleteView):
  model = Award
  success_url = '/awards/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)