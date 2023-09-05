from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('t/',views.test),
    path('',views.m),
]