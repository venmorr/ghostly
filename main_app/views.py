from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def ghost_index(request):
  return render(request, 'ghosts/index.html', { 'ghosts': ghosts })

class Ghost:  
  def __init__(self, name, level, type, description):
    self.name = name
    self.level = level
    self.type = type
    self.description = description

ghosts = [
  Ghost('Lolo', 1, 'tabby', 'Kinda rude.'),
  Ghost('Sachi', 1, 'tortoiseshell', 'Looks like a turtle.'),
  Ghost('Fancy', 1, 'bombay', 'Happy fluff ball.'),
  Ghost('Bonk', 1, 'selkirk rex', 'Meows loudly.')
]