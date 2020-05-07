from django.urls import path
from . import views

app_name = 'HomePageManager'
urlpatterns = [
    path('', views.Home.as_view(), name='HomePage'),
]