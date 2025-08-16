from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('filter/', author, name='filter'),
    path('post/', post, name='add_post'),
]