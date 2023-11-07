from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ghost

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def ghost_index(request):
  ghosts = Ghost.objects.filter(user=request.user)
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

def ghost_detail(request, ghost_id):
  ghost = Ghost.objects.get(id=ghost_id)
  return render(request, 'ghosts/detail.html', { 'ghost': ghost })

class Home(LoginView):
  template_name = 'home.html'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GhostCreate(LoginRequiredMixin, CreateView):
  model = Ghost
  fields = '__all__'
  success_url = '/ghosts/'

class GhostUpdate(UpdateView):
  model = Ghost
  fields = ['type', 'description']

class GhostDelete(DeleteView):
  model = Ghost
  success_url = '/ghosts/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('ghost-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  