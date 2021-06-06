from django.urls import path

from . import views

urlpatterns = [
    path('covidappdata', views.CovidFetchView.as_view(), name='covfetch'),
]