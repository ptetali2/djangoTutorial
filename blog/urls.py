from django.urls import path
from . import views

urlpatterns = [
    #matches each part of the url after blogs/
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]