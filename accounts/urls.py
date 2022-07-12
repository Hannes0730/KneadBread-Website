from django.urls import path
from .views import register, loginUser, logoutUser

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginUser, name='loginuser'),
    path('logout/', logoutUser, name='logoutuser'),
]