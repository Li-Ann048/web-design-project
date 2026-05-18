from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('story/', views.mrbee_story, name='mrbee_story'),
    path('characters/', views.characters, name='characters'),
    path('contact/', views.contact, name='contact'),
]