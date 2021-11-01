from django.urls import path
from .views import signinview, mainview



urlpatterns = [
    path('signin/', signinview, name='signin'),
    path('main/', mainview, name='main'),
]