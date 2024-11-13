# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.get_token, name='login'),
]
