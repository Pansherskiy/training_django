from django.urls import path
from training_django_project.article import views


urlpatterns = [
    path('', views.index),
]
