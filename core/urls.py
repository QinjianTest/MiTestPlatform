# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('test_cases/', views.list_test_cases, name='list_test_cases'),
    path('test_cases/<str:casename>/', views.test_case_detail, name='test_case_detail'),
]