from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ghost

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ghost_index(request):
  ghosts = Ghost.objects.all()
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

def ghost_detail(request, ghost_id):
  ghost = Ghost.objects.get(id=ghost_id)
  return render(request, 'ghosts/detail.html', { 'ghost': ghost })

class GhostCreate(CreateView):
  model = Ghost
  fields = '__all__'
  success_url = '/ghosts/'

class GhostUpdate(UpdateView):
  model = Ghost
  fields = ['type', 'description']

class GhostDelete(DeleteView):
  model = Ghost
  success_url = '/ghosts/'