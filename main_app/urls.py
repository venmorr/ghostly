from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('ghosts/', views.ghost_index, name='ghost-index'),
  path('ghosts/<int:ghost_id>/', views.ghost_detail, name='ghost-detail'),
]