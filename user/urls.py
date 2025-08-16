from django.urls import path
from .views import *

urlpatterns = [
    path('up/', sign_up, name='regis'),
    path('in/', sign_in, name='login'),
    path('out/', sign_out, name='logout'),
]