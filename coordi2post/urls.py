from django.urls import path
from .views import signinview, mainview, logoutview



urlpatterns = [
    path('signin/', signinview, name='signin'),
    path('main/', mainview, name='main'),
    path('logout/', logoutview, name='logout'),
]