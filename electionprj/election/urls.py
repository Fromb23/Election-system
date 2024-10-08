from django.urls import path
from . import views
from .api_views import CountyList, CountyDetail

urlpatterns = [
        path('', views.home, name='home'),
        path('registration/', views.registration, name='registration'),
        path('voter_login/', views.voter_login, name='voter_login'),
        path('search-polling-stations/', views.search_polling_stations, name='search_polling_stations'),
        path('counties/', CountyList.as_view(), name='county-view'),
        path('counties/<int:pk>', CountyDetail.as_view(), name='county-detail') 
        ]
