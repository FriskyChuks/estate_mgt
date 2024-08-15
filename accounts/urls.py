from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_view, name='auth_register'),
    path('login/', login_view, name='auth_login'),
    path('logout/', logout_view, name='auth_logout'),
    path('change_password/', change_password_view, name='change_password'),
]
