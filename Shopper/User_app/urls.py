from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_registration, name="user_registration"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('profile/', user_profile, name="user_profile"),
]
