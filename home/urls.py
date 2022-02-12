from django.urls import path

from . import views

app_name = 'home'  #namespace apki

urlpatterns = [
    path('', views.home, name='index'),
]