from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.user, name="user"),
    path("voter", views.voter, name="voter"),
    path('', views.index, name='index')
]