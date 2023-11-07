from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('ghosts/', views.ghost_index, name='ghost-index'),
  path('ghosts/<int:ghost_id>/', views.ghost_detail, name='ghost-detail'),
  path('ghosts/create/', views.GhostCreate.as_view(), name='ghost-create'),
  path('ghosts/<int:pk>/update/', views.GhostUpdate.as_view(), name='ghost-update'),
  path('ghosts/<int:pk>/delete/', views.GhostDelete.as_view(), name='ghost-delete'),
]