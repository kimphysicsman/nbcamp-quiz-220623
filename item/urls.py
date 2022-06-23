from django.contrib import admin
from django.urls import path
from . import views

# item/
urlpatterns = [
    path('', views.ItemView.as_view()),
    path('order/', views.OrderView.as_view()),
]