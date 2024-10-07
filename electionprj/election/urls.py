from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('registration/', views.registration, name='registration'),
        path('voter_login/', views.voter_login, name='voter_login')
        ]
