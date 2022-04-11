from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path("accounts/", include("django.contrib.auth.urls")),  

]
