from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:post_id>/', views.detail, name="detail"),
    # path('new/', views.new, name="new"),
    path('search/', views.search, name="search"),
]
