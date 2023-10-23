from django.contrib import admin
from django.urls import path, include
from .views import UserProductView


urlpatterns = [
    path('', UserProductView.as_view(), name='shop')
]