from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.DetailCarView.as_view(), name='car_detail'),
]
