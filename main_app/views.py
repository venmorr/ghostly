from django.shortcuts import render
from .models import Ghost

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ghost_index(request):
  ghosts = Ghost.objects.all()
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

ghosts = [
  Ghost('Lolo', 2, 'tabby', 'Kinda rude.'),
  Ghost('Sachi', 3, 'tortoiseshell', 'Looks like a turtle.'),
  Ghost('Fancy', 4, 'bombay', 'Happy fluff ball.'),
  Ghost('Bonk', 1, 'selkirk rex', 'Meows loudly.')
]