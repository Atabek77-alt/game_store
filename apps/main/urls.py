from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('search/', search_by_title, name='search_by_title1'),
]
