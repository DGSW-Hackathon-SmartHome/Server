from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getAllSensor),
    path('control_temp/', views.control_temp),
]