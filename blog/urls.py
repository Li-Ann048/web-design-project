from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('story/', views.story_list, name='story_list'),
    path('story/<slug:slug>/', views.story_detail, name='story_detail'),
    path('characters/', views.characters, name='characters'),
    path('contact/', views.contact, name='contact'),
]